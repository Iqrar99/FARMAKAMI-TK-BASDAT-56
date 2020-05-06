from django.shortcuts import render

# Create your views here.
def konsumen_nav(request):
    context = {

    }

    return render(request, 'navigation/konsumen.html', context)