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

def update_pengantaran_farmasi(request):
	context = {
        'form' : UpdatePengantaranForm(request.POST or None)
    }
	return render(request, 'update/update_pengantaran_farmasi.html', context)

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

def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
