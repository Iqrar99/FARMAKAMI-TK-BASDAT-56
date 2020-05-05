from django.urls import path, include
from . import views

urlpatterns = [
    path("konsumen/", views.konsumen_nav, name='konsumen_nav'),
]
