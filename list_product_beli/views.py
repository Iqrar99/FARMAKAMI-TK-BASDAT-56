from django.shortcuts import render
from django.db import connection
from .forms import ListProdukForm, UpdateList

# Create your views here.
def tabel_list_produk_dibeli(request):
    query = """SELECT * FROM list_produk_dibeli;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_list_produk = fetch(cursor)

    context = {
        'data_list_produk': data_list_produk,
        'role': request.session['role']
    }

    return render(request, 'tabel/read_list_produk_dibeli.html', context)

def create_list_produk_dibeli(request):
	context = {
        'form' : ListProdukForm(request.POST or None)
    }
	return render(request, 'create/create_list_produk_dibeli.html', context)

def update_list_produk_dibeli(request):
	context = {
        'form' : UpdateList(request.POST or None)
    }
	return render(request, 'update/update_list_product_dibeli.html', context)


def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
