from django.shortcuts import render

# Create your views here.
def tabel_apotek(request):
	context = {}
	return render(request, 'tabel/read_apotek.html', context)

def buat_apotek(request):
	context = {}
	return render(request, 'create/create_apotek.html', context)

