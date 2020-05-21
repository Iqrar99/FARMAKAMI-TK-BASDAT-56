from django.shortcuts import render
from django.db import connection
from .forms import CreateBalaiPengobatanForm, UpdateBalaiPengobatanForm 

# Create your views here.
def tabel_balai_pengobatan(request):
    query = """SELECT * FROM balai_pengobatan;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_balai = fetch(cursor)
    
    context = {
        'data_balai' : data_balai
    }

    return render(request, 'tabel/read_balai_pengobatan.html', context)

def buat_balai_pengobatan(request):
    context = {
        'form' : CreateBalaiPengobatanForm(request.POST or None)
    }
        
    return render(request, 'create/create_balai_pengobatan.html', context)

def update_balai_pengobatan(request):
    context = {
        'form' : UpdateBalaiPengobatanForm(request.POST or None)
    }

    return render(request, 'update/update_balai_pengobatan.html', context)

def fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
