from django.urls import path, include
from . import views

urlpatterns = [
    path("tabel/", views.tabel_transaksi_pembelian, name='transaksi_pembelian'),
    path("buat/", views.buat_transaksi_pembelian, name='transaksi_pembelian'),
]
