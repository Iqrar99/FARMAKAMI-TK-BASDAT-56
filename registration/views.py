from django.shortcuts import render, reverse

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
    context = {}

    return render(request, 'register_admin.html', context)


def register_consumer(request):
    context = {}

    return render(request, 'register_consumer.html', context)


def register_kurir(request):
    context = {}

    return render(request, 'register_kurir.html', context)


def register_cs(request):
    context = {}

    return render(request, 'register_cs.html', context)
