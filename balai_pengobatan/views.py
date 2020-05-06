from django.shortcuts import render
from .forms import CreateBalaiPengobatanForm, UpdateBalaiPengobatanForm 

# Create your views here.
def tabel_balai_pengobatan(request):
    context = {}

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