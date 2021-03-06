from django.urls import path, include
from . import views

urlpatterns = [
    path("tabel/", views.tabel_obat, name='tabel_obat'),
    path("buat/", views.buat_obat, name='buat_obat'),
    path("update/<str:id>", views.update_obat, name='update_obat'),
    path("tabel/delete/", views.delete_obat)
]
