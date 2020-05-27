from django.shortcuts import render, redirect
from django.db import connection
from datetime import datetime
from .forms import TransaksiPembelianForm, UpdateTransaksiPembelian

def tabel_transaksi_pembelian(request):
    if 'email' not in request.session:
        return redirect('/login/')

    nama = ""
    
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    if request.session['role'] == 'konsumen': 
        query = f"""
            SELECT * FROM transaksi_pembelian
            WHERE id_konsumen = '{get_id_konsumen(request)}';
        """
        cursor.execute(query)

        nama = request.session['nama']
    
    else:
        query = """SELECT * FROM transaksi_pembelian;"""
        cursor.execute(query)

    data_transaksi_pembelian = __fetch(cursor)
    
    context = {
        'data_transaksi_pembelian' : data_transaksi_pembelian,
        'role' : request.session['role'],
        'nama' : nama
    }

    return render(request, 'tabel/read_transaksi_pembelian.html', context)

def buat_transaksi_pembelian(request):
    if 'email' not in request.session:
        return redirect('/login/')

    if request.session['role'] != 'admin-apotek':
        return redirect(f'/navigate/{request.session["role"]}/')

    form = TransaksiPembelianForm(request.POST or None)
    context = {
        'form': form,
        'error': []
    }

    id_konsumen = request.POST['id_konsumen']

    try:
        __create_transaksi_beli(id_konsumen)
        print("TRANSAKSI PEMBELIAN SUKSES DITAMBAHKAN")
        
        return redirect('/transaksi-pembelian/tabel/')

    except:
        print("TRANSAKSI PEMBELIAN GAGAL DITAMBAHKAN")

    return render(request, 'create/create_transaksi_pembelian.html', context)

def update_transaksi_pembelian(request):
    context = {
        'form': UpdateTransaksiPembelian(request.POST or None)
    }
    return render(request, 'update/update_transaksi_pembelian.html', context)

def get_id_konsumen(request):
    """
    function untuk mendapatkan id konsumen
    berdasarkan konsumen yang sedang login.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    email = request.session['email']
    cursor.execute(
        f"""
        SELECT id_konsumen FROM konsumen
        WHERE email = '{email}';
        """
    )

    id_konsumen = __fetch(cursor)[0]
    return id_konsumen['id_konsumen']

def __create_transaksi_beli(id_konsumen):
    """
    function untuk menambah transaksi pembelian baru.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
     
    # generate id transaksi
    cursor.execute(
        """
        SELECT id_transaksi_pembelian FROM transaksi_pembelian
        ORDER BY id_transaksi_pembelian DESC
        LIMIT 1;
        """
    )
    latest_id = int(__fetch(cursor)[0]['id_transaksi_pembelian'][-3:])
    new_id = latest_id + 1
    if new_id < 10:
        new_id = 'T00' + str(new_id)
    elif new_id < 100:
        new_id = 'T0' + str(new_id)
    else:
        new_id = 'T' + str(new_id)

    waktu_pembelian = str(datetime.now())

    cursor.execute(
        f"""
        INSERT INTO transaksi_pembelian
        VALUES ('{new_id}', '{waktu_pembelian}', 0, '{id_konsumen}');
        """
    )

def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
