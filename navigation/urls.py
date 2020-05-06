from django.urls import path, include
from . import views

urlpatterns = [
	path("admin-apotek/", views.admin_apotek_nav, name='admin_apotek_nav'),
	path("cs/", views.cs_nav, name='cs_nav'),
 	path("konsumen/", views.konsumen_nav, name='konsumen_nav'),
 	path("kurir/", views.kurir_nav, name='kurir_nav'),
]
