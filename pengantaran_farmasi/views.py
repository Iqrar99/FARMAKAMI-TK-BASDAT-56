from django.shortcuts import render
from .forms import PengantaranForm 

# Create your views here.
def tabel_pengantaran_farmasi(request):
    context = {}
    return render(request, 'tabel/read_pengantaran_farmasi.html', context)

def create_pengantaran_farmasi(request):
	context = {
        'form' : PengantaranForm(request.POST or None)
    }
	return render(request, 'create/create_pengantaran_farmasi.html', context)
