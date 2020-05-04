from django.shortcuts import render, reverse
from .forms import AdminForm, ConsumerForm, KurirForm, CSForm

# Create your views here.
def main_menu_register(request):
    context = {
        'register_admin' : reverse('register_admin'),
        'register_consumer' : reverse('register_consumer'),
        'register_kurir' : reverse('register_kurir'),
        'register_cs' : reverse('register_cs'),
    }

    return render(request, 'register.html', context)

def register_admin(request):
    context = {
        'form' : AdminForm(request.POST or None)
    }

    return render(request, 'register_admin.html', context)


def register_consumer(request):
    context = {
        'form' : ConsumerForm(request.POST or None)
    }

    return render(request, 'register_consumer.html', context)


def register_kurir(request):
    context = {
        'form' : KurirForm(request.POST or None)
    }

    return render(request, 'register_kurir.html', context)


def register_cs(request):
    context = {
        'form' : CSForm(request.POST or None)
    }

    return render(request, 'register_cs.html', context)
