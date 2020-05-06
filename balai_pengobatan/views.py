from django.shortcuts import render
from .forms import BalaiPengobatanForm 

# Create your views here.
def tabel_balai_pengobatan(request):
    context = {}

    return render(request, 'tabel/read_balai_pengobatan.html', context)

def buat_balai_pengobatan(request):
    context = {
        'form' : BalaiPengobatanForm(request.POST or None)
    }
        
    return render(request, 'create/create_balai_pengobatan.html', context)