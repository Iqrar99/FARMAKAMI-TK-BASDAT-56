from django.shortcuts import render

# Create your views here.
def main_menu_register(request):

    context = {}

    return render(request, 'register.html', context)