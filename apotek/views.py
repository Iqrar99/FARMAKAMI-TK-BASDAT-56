from django.shortcuts import render, redirect
from django.db import connection
from .forms import CreateApotekForm, UpdateApotekForm

def tabel_apotek(request):
	query = """SELECT * FROM apotek;"""
	
	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")
	cursor.execute(query)

	data_apotek = __fetch(cursor)

	context = {
		'data_apotek' : data_apotek,
		'role' : request.session['role']
	}
	
	return render(request, 'tabel/read_apotek.html', context)

def buat_apotek(request):
	if 'email' not in request.session:
    	 return redirect('/login/')

	if request.session['role'] != 'admin-apotek':
		return redirect(f'/navigate/{request.session["role"]}/')

	form = CreateApotekForm(request.POST or None)
	context = {
        'form': form,
        'error': []
    }

	if (request.method == 'POST' and form.is_valid()):
		valid = True

		email = request.POST['email_penyelenggara']
		nama_penyelenggara = request.POST['nama_penyelenggara']
		nama_apotek = request.POST['nama_apotek']
		alamat = request.POST['alamat_apotek']

		# validasi no telp
		telp = request.POST['telepon_apotek']
		if not telp.isnumeric():
			context['error'].append(
				'The phone number should contains number only.')
			valid = valid and False

		# validasi no SIA
		no_sia = request.POST['no_sia']
		if not no_sia.isnumeric():
			context['error'].append(
				'The SIA number should contains number only.')
			valid = valid and False
		
		if valid:

			try:
				__create_apotek(email, no_sia, nama_penyelenggara, nama_apotek, alamat, telp)
				print("APOTEK SUKSES DIBUAT")
				return redirect('/apotek/tabel/')

			except:
				print("APOTEK GAGAL DIBUAT")
	
	return render(request, 'create/create_apotek.html', context)

def update_apotek(request):
	context = {
        'form' : UpdateApotekForm(request.POST or None)
    }
	return render(request, 'update/update_apotek.html', context)

def __create_apotek(email, no_sia, nama_penyelenggara, nama_apotek, alamat, telp):
	"""
	function untuk membuat apotek baru.
	"""
	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")

	# generate id apotek
	cursor.execute(
        """
        SELECT id_apotek FROM apotek
        ORDER BY id_apotek DESC
        LIMIT 1;
        """
    )
	latest_id = int(__fetch(cursor)[0]['id_apotek'][-2:])
	new_id = latest_id + 1
	if new_id < 10:
	    new_id = 'AP0' + str(new_id)
	else:
	    new_id = 'AP' + str(new_id)

	cursor.execute(
		f"""
		INSERT INTO apotek
		VALUES ('{new_id}', '{email}', '{no_sia}', '{nama_penyelenggara}', 
		'{nama_apotek}', '{alamat}', '{telp}');
		"""
	)

def __fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
