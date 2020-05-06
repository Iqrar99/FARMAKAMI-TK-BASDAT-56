from django.urls import path, include
from . import views

urlpatterns = [
    path("tabel/", views.tabel_pengantaran_farmasi, name='tabel_pengantaran_farmasi'),
    path("buat/", views.create_pengantaran_farmasi, name='buat_list_produk_dibeli'),
    path("update/", views.update_pengantaran_farmasi, name='update_pengantaran_farmasi'),
]