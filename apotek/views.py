from django.shortcuts import render
from .forms import CreateApotekForm, UpdateApotekForm

# Create your views here.
def tabel_apotek(request):
	context = {}
	
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
