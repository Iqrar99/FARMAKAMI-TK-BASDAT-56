from django.shortcuts import render
from django.db import connection
from .forms import CreateApotekForm, UpdateApotekForm

# Create your views here.
def tabel_apotek(request):
	query = """SELECT * FROM apotek;"""
	
	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")
	cursor.execute(query)

	data_apotek = fetch(cursor)

	context = {
		'data_apotek' : data_apotek,
		'role' : request.session['role']
	}
	
	return render(request, 'tabel/read_apotek.html', context)

def buat_apotek(request):
	context = {
        'form' : CreateApotekForm(request.POST or None)
    }
	return render(request, 'create/create_apotek.html', context)

def update_apotek(request):
	context = {
        'form' : UpdateApotekForm(request.POST or None)
    }
	return render(request, 'update/update_apotek.html', context)

def fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
