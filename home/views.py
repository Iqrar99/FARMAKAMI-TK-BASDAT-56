from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):
    context = { 
        'login_page' : reverse('user_login')
    }

    return render(request, 'homepage.html', context)