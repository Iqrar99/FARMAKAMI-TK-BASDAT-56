from django.shortcuts import render

# Create your views here.
def tabel_produk_apotek(request):
	context = {}
	return render(request, 'tabel/read_produk_apotek.html', context)

def buat_produk_apotek(request):
	context = {}
	return render(request, 'create/create_produk_apotek.html', context)

