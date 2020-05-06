from django.shortcuts import render
from .forms import ListProdukForm 

# Create your views here.
def tabel_list_produk_dibeli(request):
    context = {}
    return render(request, 'tabel/read_list_produk_dibeli.html', context)

def create_list_produk_dibeli(request):
	context = {
        'form' : ListProdukForm(request.POST or None)
    }
	return render(request, 'create/create_list_produk_dibeli.html', context)
