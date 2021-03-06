from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def home(request):

    if 'email' in request.session:
        return redirect(f"/navigate/{request.session['role']}")

    context = { 
        'login_page' : reverse('user_login'),
        'register_page' : reverse('main_menu_register'),
    }

    return render(request, 'homepage.html', context)
