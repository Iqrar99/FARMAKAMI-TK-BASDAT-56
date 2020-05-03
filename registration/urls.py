from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main_menu_register, name = 'main_menu_register'),
    path("admin/", views.register_admin, name = 'register_admin'),
    path("consumer/", views.register_consumer, name = 'register_consumer'),
    path("kurir/", views.register_kurir, name = 'register_kurir'),
    path("cs/", views.register_cs, name = 'register_cs'),
]
 