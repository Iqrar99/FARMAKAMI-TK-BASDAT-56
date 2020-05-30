from django.urls import path, include
from . import views

urlpatterns = [
	path("tabel/", views.tabel_produk_apotek, name='tabel_produk_apotek'),
	path("buat/", views.buat_produk_apotek, name='buat_produk_apotek'),
	path("update/<str:idproduk>/<str:idapotek>", views.update_produk_apotek, name='update_produk_apotek'),
	path("tabel/delete/", views.delete_produk_apotek)
]
