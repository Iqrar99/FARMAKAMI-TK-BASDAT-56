from django.urls import path, include
from . import views

urlpatterns = [
    path("tabel/", views.data_balai_pengobatan, name='balai_pengobatan'),
]