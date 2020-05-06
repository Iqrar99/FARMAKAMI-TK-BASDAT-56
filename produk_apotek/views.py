from django.shortcuts import render
from .forms import CreateProdukApotekForm, UpdateProdukApotekForm 

# Create your views here.
def tabel_produk_apotek(request):
	context = {}
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


