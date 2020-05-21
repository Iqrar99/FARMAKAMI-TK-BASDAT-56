from django.shortcuts import render
from django.db import connection
from .forms import CreateObatForm, UpdateObatForm

# Create your views here.
def tabel_obat(request):
    query = """SELECT * FROM obat;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_obat = fetch(cursor)

    context = {
        'data_obat': data_obat
    }

    return render(request, 'tabel/read_obat.html', context)

def buat_obat(request):
    context = {
        'form' : CreateObatForm(request.POST or None)
    }

    return render(request, 'create/create_obat.html', context)

def update_obat(request):
    context = {
        'form' : UpdateObatForm(request.POST or None)
    }

    return render(request, 'update/update_obat.html', context)

def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
