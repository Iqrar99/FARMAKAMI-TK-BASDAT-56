from django.shortcuts import render
from .forms import ObatForm

# Create your views here.
def tabel_obat(request):
    context = {}

    return render(request, 'tabel/read_obat.html', context)

def buat_obat(request):
    context = {
        'form' : ObatForm(request.POST or None)
    }

    return render(request, 'create/create_obat.html', context)