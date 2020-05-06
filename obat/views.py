from django.shortcuts import render
from .forms import CreateObatForm, UpdateObatForm

# Create your views here.
def tabel_obat(request):
    context = {}

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