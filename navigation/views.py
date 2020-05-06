from django.shortcuts import render

# Create your views here.
def admin_apotek_nav(request):
	context = {
	}
	return render(request, 'navigation/admin_apotek.html', context)

def cs_nav(request):
	context = {
	}
	return render(request, 'navigation/cs.html', context)

def konsumen_nav(request):
	context = {
	}
	return render(request, 'navigation/konsumen.html', context)

def kurir_nav(request):
	context = {
	}
	return render(request, 'navigation/kurir.html', context)