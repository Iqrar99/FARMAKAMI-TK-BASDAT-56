from django.shortcuts import render
from django.db import connection
from .forms import PengantaranForm,UpdatePengantaranForm

# Create your views here.
def tabel_pengantaran_farmasi(request):
    query = """SELECT * FROM pengantaran_farmasi;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_pengantaran = fetch(cursor)

    context = {
        'data_pengantaran': data_pengantaran,
        'role': request.session['role']
    }

    return render(request, 'tabel/read_pengantaran_farmasi.html', context)

def create_pengantaran_farmasi(request):
	context = {
        'form' : PengantaranForm(request.POST or None)
    }
	return render(request, 'create/create_pengantaran_farmasi.html', context)

def update_pengantaran_farmasi(request):
	context = {
        'form' : UpdatePengantaranForm(request.POST or None)
    }
	return render(request, 'update/update_pengantaran_farmasi.html', context)

def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
