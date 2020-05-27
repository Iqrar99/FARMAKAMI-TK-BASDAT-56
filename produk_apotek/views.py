from django.shortcuts import render, redirect
from django.db import connection, IntegrityError
from .forms import CreateProdukApotekForm, UpdateProdukApotekForm

# Create your views here.
def tabel_produk_apotek(request):
	if 'email' not in request.session:
		return redirect('/login/')

	query = """SELECT * FROM produk_apotek;"""

	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")
	cursor.execute(query)

	data_produk_apotek = __fetch(cursor)

	context = {
	    'data_produk_apotek' : data_produk_apotek,
	    'role': request.session['role']
	}

	return render(request, 'tabel/read_produk_apotek.html', context)

def buat_produk_apotek(request):
	"""
	function untuk menambahkan data produk apotek.
	"""

	if 'email' not in request.session:
		return redirect('/login/')

	if request.session['role'] != 'admin-apotek':
	    return redirect(f'/navigate/{request.session["role"]}/')

	form = CreateProdukApotekForm(request.POST or None)
	context = {
	    'form': form,
	    'error': []
	}

	if (request.method == 'POST' and form.is_valid()):
		valid = True

		print(request.POST)

		id_produk = request.POST['id_produk']
		id_apotek = request.POST['id_apotek']
		satuan = request.POST['satuan_penjualan'] 

		# validasi harga
		harga = request.POST['harga_jual']
		if int(harga) < 0:
			valid = valid and False
			context['error'].append('Harga Jual can not be negative.')

		# validasi stok
		stok = request.POST['stok'] 
		if int(stok) < 0:
			valid = valid and False
			context['error'].append('Stok can not be negative.')

		if valid:
			try:
				__create_produk_apotek(harga, stok, satuan, id_produk, id_apotek)
				print("PRODUK APOTEK SUKSES DITAMBAHKAN")
				return redirect('/produk-apotek/tabel/')

			except IntegrityError as integrity:
				context['error'].append(integrity)
				print("PRODUK APOTEK GAGAL DITAMBAHKAN")
			
			except:
				print("PRODUK APOTEK GAGAL DITAMBAHKAN")

	return render(request, 'create/create_produk_apotek.html', context)

def update_produk_apotek(request):
	context = {
        'form' : UpdateProdukApotekForm(request.POST or None)
    }
	return render(request, 'update/update_produk_apotek.html', context)

def __create_produk_apotek(harga, stok, satuan, id_produk, id_apotek):
	"""
	function untuk menambahkan produk apotek ke database.
	"""
	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")

	cursor.execute(
		f"""
		INSERT INTO produk_apotek
		VALUES ({harga}, {stok}, '{satuan}', '{id_produk}', '{id_apotek}');
		"""
	)

def __fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
