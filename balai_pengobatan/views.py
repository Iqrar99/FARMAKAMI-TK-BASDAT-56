from django.shortcuts import render

# Create your views here.
def data_balai_pengobatan(request):
    context = {}

    return render(request, 'tabel/balai_pengobatan.html', context)
