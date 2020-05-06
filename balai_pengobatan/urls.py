from django.urls import path, include
from . import views

urlpatterns = [
    path("tabel/", views.tabel_balai_pengobatan, name='tabel_balai_pengobatan'),
    path("buat/", views.buat_balai_pengobatan, name='buat_balai_pengobatan'),
    path("update/", views.update_balai_pengobatan, name='update_balai_pengobatan')
]