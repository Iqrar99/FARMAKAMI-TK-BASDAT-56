from django.urls import path, include
from . import views

urlpatterns = [
	path("tabel/", views.tabel_apotek, name='tabel_apotek'),
	path("buat/", views.buat_apotek, name='buat_apotek'),
	path("update/<str:id>", views.update_apotek, name='update_apotek'),
	path("tabel/delete/", views.delete_apotek),
]