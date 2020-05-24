from django.shortcuts import render
from django.db import connection
from .forms import TransaksiPembelianForm, UpdateTransaksiPembelian
# Create your views here.


def tabel_transaksi_pembelian(request):
    query = """SELECT * FROM transaksi_pembelian;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_transaksi_pembelian = fetch(cursor)
    
    context = {
        'data_transaksi_pembelian' : data_transaksi_pembelian,
        'role': request.session['role']
    }

    return render(request, 'tabel/read_transaksi_pembelian.html', context)

def buat_transaksi_pembelian(request):
    context = {
        'form': TransaksiPembelianForm(request.POST or None)
    }
    return render(request, 'create/create_transaksi_pembelian.html', context)


def update_transaksi_pembelian(request):
    context = {
        'form': UpdateTransaksiPembelian(request.POST or None)
    }
    return render(request, 'update/update_transaksi_pembelian.html', context)


def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
