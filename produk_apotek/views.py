from django.shortcuts import render
from django.db import connection
from .forms import CreateProdukApotekForm, UpdateProdukApotekForm 

# Create your views here.
def tabel_produk_apotek(request):
	query = """SELECT * FROM produk_apotek;"""

	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")
	cursor.execute(query)

	data_produk_apotek = fetch(cursor)

	context = {
	    'data_produk_apotek' : data_produk_apotek,
	    'role': request.session['role']
	}

	return render(request, 'tabel/read_produk_apotek.html', context)

def buat_produk_apotek(request):
	context = {
        'form' : CreateProdukApotekForm(request.POST or None)
    }
	return render(request, 'create/create_produk_apotek.html', context)

def update_produk_apotek(request):
	context = {
        'form' : UpdateProdukApotekForm(request.POST or None)
    }
	return render(request, 'update/update_produk_apotek.html', context)


def fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
