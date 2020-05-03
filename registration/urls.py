from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main_menu_register, name = 'main_menu_register'),
]
