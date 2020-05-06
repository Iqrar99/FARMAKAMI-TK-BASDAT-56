from django.shortcuts import render
from .forms import ApotekForm 

# Create your views here.
def tabel_apotek(request):
	context = {}
	return render(request, 'tabel/read_apotek.html', context)

def buat_apotek(request):
	context = {
        'form' : ApotekForm(request.POST or None)
    }
	return render(request, 'create/create_apotek.html', context)

