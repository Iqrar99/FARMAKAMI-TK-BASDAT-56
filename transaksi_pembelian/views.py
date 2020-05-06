from django.shortcuts import render
from .forms import TransaksiPembelianForm
# Create your views here.


def tabel_transaksi_pembelian(request):
    context = {}
    return render(request, 'tabel/read_transaksi_pembelian.html', context)


def buat_transaksi_pembelian(request):
    context = {
        'form': TransaksiPembelianForm(request.POST or None)
    }
    return render(request, 'create/create_transaksi_pembelian.html', context)
