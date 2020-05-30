from django.shortcuts import render, redirect
from django.db import connection
from .forms import PengantaranForm,UpdatePengantaranForm
import random

# Create your views here.
def tabel_pengantaran_farmasi(request):
    if 'email' not in request.session:
        return redirect('/login/')

    query = """SELECT * FROM pengantaran_farmasi;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_pengantaran = __fetch(cursor)

    context = {
        'data_pengantaran': data_pengantaran,
        'role': request.session['role']
    }

    return render(request, 'tabel/read_pengantaran_farmasi.html', context)

def create_pengantaran_farmasi(request):
    if 'email' not in request.session:
        return redirect('/login/')

    if request.session['role'] != 'admin-apotek':
        return redirect(f'/navigate/{request.session["role"]}/')
    
    form = PengantaranForm(request.POST or None)
    context = {
        'form': form,
        'error': []
    }
    
    if (request.method == 'POST' and form.is_valid()):
        valid = True

        id_transaksi = request.POST['id_transaksi']
        waktu = request.POST['waktu']

        # validasi biaya kirim
        biaya = request.POST['biaya_kirim']
        if int(biaya) <= 0:
            valid = valid and False
            context['error'].append('Biaya Kirim must be positive.')

        if valid:
            try:
                __create_pengantaran(id_transaksi, waktu, biaya)
                print("PENGANTARAN BERHASIL DITAMBAHKAN")
                return redirect('/pengantaran-farmasi/tabel/')

            except:
                
                print("PENGANTARAN GAGAL DITAMBAHKAN")
                

    return render(request, 'create/create_pengantaran_farmasi.html', context)

def update_pengantaran_farmasi(request,idpengantaran,totalbiaya):
    if 'email' not in request.session:
        return redirect('/login/')
    
    if (request.session['role'] != 'admin-apotek'):
        return redirect(f'/navigate/{request.session["role"]}/')

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(f"SELECT * FROM pengantaran_farmasi")
    
    data_pengantaran = {}
    x = __fetch(cursor)

    for i in range(len(x)):
        if x[i]['id_pengantaran'] == idpengantaran:
            data_pengantaran = x[i]
            break


    data_id_kurir = __get_id_kurir()
    data_id_transaksi_pembelian = __get_id_transaksi()
    data_waktu = data_pengantaran['waktu'].strftime("%Y-%m-%d %H:%M:%S")
    data_status = data_pengantaran['status_pengantaran']
    data_biaya_kirim = data_pengantaran['biaya_kirim']

    form = UpdatePengantaranForm(request.POST or None, initial = {
        'id_pengantaran' : idpengantaran,
        'id_kurir': data_id_kurir,
        'id_transaksi' : data_id_transaksi_pembelian,
        'waktu' : data_waktu,
        'status_pengiriman' : data_status,
        'biaya_kirim': data_biaya_kirim,
        'total_biaya': totalbiaya,
    })

    context={
        'error': [],
        'form': form,
    }
    if (request.method == 'POST' and form.is_valid()):
        valid = True

        id_pengantaran = idpengantaran
        id_kurir= request.POST['id_kurir']
        id_transaksi_pembelian=request.POST['id_transaksi']
        waktu=request.POST['waktu']
        status_pengiriman=request.POST['status_pengiriman']
        biaya_kirim=request.POST['biaya_kirim']
        total_biaya=totalbiaya


        if (biaya_kirim != '' and (not biaya_kirim.isnumeric())):
            context['error'].append(
                'Masukkan angka yang benar')
            valid = valid and False
        
        if valid:
            __update(id_pengantaran, id_kurir, id_transaksi_pembelian, waktu, status_pengiriman, biaya_kirim, total_biaya)
            try:

                print("UPDATE SUKSES")
                return redirect('/pengantaran-farmasi/tabel/')

            except:
                print("UPDATE GAGAL")

    return render(request, 'update/update_pengantaran_farmasi.html', context)


def delete_pengantaran(request):
    """
    function untuk menghapus data pengantaran farmasi.
    """
    id_pengantaran = request.POST['id_pengantaran']

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        DELETE FROM pengantaran_farmasi
        WHERE id_pengantaran = '{id_pengantaran}';
        """
    )

    return redirect('/pengantaran-farmasi/tabel/')

def __create_pengantaran(id_transaksi, waktu, biaya):
    """
    function untuk menambahkan data pengantaran baru.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    # generate id pengantaran
    cursor.execute(
        """
        SELECT id_pengantaran FROM pengantaran_farmasi
        ORDER BY id_pengantaran DESC
        LIMIT 1;
        """
    )
    latest_id = int(__fetch(cursor)[0]['id_pengantaran'][-2:])
    new_id = latest_id + 1
    if new_id < 10:
        new_id = 'PE0' + str(new_id)
    else:
        new_id = 'PE' + str(new_id)

    # choose random kurir as default kurir
    cursor.execute("SELECT id_kurir FROM kurir;")
    data = [row for row in cursor.fetchall()]
    id_kurir_default = random.choice(data)[0]

    cursor.execute(
        f"""
        INSERT INTO pengantaran_farmasi
        VALUES ('{new_id}', '{id_kurir_default}', '{id_transaksi}', '{waktu}',
        'MENUNGGU', {biaya}, {biaya});
        """
    )

def __get_id_transaksi():
    """
    function untuk mendapatkan id transaksi yang telah terdaftar
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        SELECT id_transaksi_pembelian FROM transaksi_pembelian
        """
    )

    return __fetch(cursor)[0]['id_transaksi_pembelian']

def __get_id_kurir():
    """
    function untuk mendapatkan id kurir yang telah terdaftar
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        SELECT id_kurir FROM kurir
        """
    )

    return __fetch(cursor)[0]['id_kurir']



def __update(id_pengantaran, id_kurir, id_transaksi_pembelian, waktu, status_pengantaran, biaya_kirim, total_biaya):
    """
    function untuk memperbarui data pengantaran farmasi.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        UPDATE pengantaran_farmasi
        SET (id_kurir, id_transaksi_pembelian, waktu, status_pengantaran, biaya_kirim) = ('{id_kurir}','{id_transaksi_pembelian}','{waktu}','{status_pengantaran}','{biaya_kirim}')
        WHERE total_biaya = '{total_biaya}' and id_pengantaran='{id_pengantaran}';
        """
    )

def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
