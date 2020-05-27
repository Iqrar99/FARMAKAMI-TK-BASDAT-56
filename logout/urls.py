from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.user_logout, name='user_logout'),
    path("backHome", views.back_home)
]
