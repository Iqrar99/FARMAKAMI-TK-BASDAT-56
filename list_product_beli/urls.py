from django.urls import path, include
from . import views

urlpatterns = [
    path("tabel/", views.tabel_list_produk_dibeli, name='tabel_list_produk_dibeli'),
    path("buat/", views.create_list_produk_dibeli, name='buat_list_produk_dibeli'),
    path("update/<str:idproduk>/<str:idapotek>", views.update_list_produk_dibeli, name='update_list_produk_dibeli'),
    path("tabel/delete/", views.delete_produk_dibeli),
]