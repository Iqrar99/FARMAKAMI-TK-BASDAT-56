from django.shortcuts import render, redirect

# Create your views here.
def admin_apotek_nav(request):
	context = {}

	if 'nama' in request.session:
		if request.session['role'] == 'admin-apotek':
			context['nama'] = request.session['nama']
		else:
			return redirect(f"/navigate/{request.session['role']}")
	else:
		return redirect('/')

	return render(request, 'navigation/admin_apotek.html', context)

def cs_nav(request):
	context = {}

	if 'nama' in request.session:
		if request.session['role'] == 'cs':
			context['nama'] = request.session['nama']
		else:
			return redirect(f"/navigate/{request.session['role']}")
	else:
		return redirect('/')

	return render(request, 'navigation/cs.html', context)

def konsumen_nav(request):
	context = {}

	if 'nama' in request.session:
		if request.session['role'] == 'konsumen':
			context['nama'] = request.session['nama']
		else:
			return redirect(f"/navigate/{request.session['role']}")
	else:
		return redirect('/')

	return render(request, 'navigation/konsumen.html', context)

def kurir_nav(request):
	context = {}

	if 'nama' in request.session:
		if request.session['role'] == 'kurir':
			context['nama'] = request.session['nama']
		else:
			return redirect(f"/navigate/{request.session['role']}")
	else:
		return redirect('/')
	
	return render(request, 'navigation/kurir.html', context)
