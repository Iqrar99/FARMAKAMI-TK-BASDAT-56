from django.shortcuts import render, redirect
from django.db import connection, IntegrityError
from .forms import CreateProdukApotekForm, UpdateProdukApotekForm

# Create your views here.
def tabel_produk_apotek(request):
	"""
    function untuk menampilkan data produk apotek.
    """
	if 'email' not in request.session:
		return redirect('/login/')

	query = """SELECT * FROM produk_apotek ORDER BY id_produk ASC;"""

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
	function untuk membuat data produk apotek.
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


def update_produk_apotek(request, idproduk, idapotek):
	
	if 'email' not in request.session:
		return redirect('/login/')

	if(request.session['role'] != 'admin-apotek'):
		return redirect(f'/navigate/{request.session["role"]}/')

    # Panggil data initial pada form

	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")
	cursor.execute(f"SELECT * FROM produk_apotek")

	data_produk_apotek = {}
	x = __fetch(cursor)
	for i in range(len(x)):
		if x[i]['id_produk'] == idproduk and x[i]['id_apotek'] == idapotek:
			data_produk_apotek = x[i]
			break

	data_harga_jual = data_produk_apotek['harga_jual']
	data_satuan_penjualan = data_produk_apotek['satuan_penjualan']
	data_stok = data_produk_apotek['stok']

	form = UpdateProdukApotekForm(request.POST or None, initial = {
		'id_produk' : idproduk,
		'id_apotek' : idapotek,
		'harga_jual': data_harga_jual,
		'satuan_penjualan' : data_satuan_penjualan,
		'stok' : data_stok
	})

	context = {
		'error': [],
		'form': form,
    }


	if (request.method == 'POST' and form.is_valid()):
		valid = True

		id_produk = idproduk
		id_apotek = idapotek
		harga_jual = request.POST['harga_jual']
		satuan_penjualan = request.POST['satuan_penjualan']
		stok = request.POST['stok']
        
       	# validasi harga
		if int(harga_jual) < 0:
			valid = valid and False
			context['error'].append('Harga Jual can not be negative.')

		# validasi stok
		if int(stok) < 0:
			valid = valid and False
			context['error'].append('Stok can not be negative.')

		if valid:
			try:
				__update(id_produk, id_apotek, harga_jual, satuan_penjualan, stok)
				print("UPDATE PRODUK APOTEK SUKSES")
				return redirect('/produk-apotek/tabel/')

			except IntegrityError as integrity:
				context['error'].append(integrity)
				print("UPDATE PRODUK APOTEK GAGAL")

			except:
				print("UPDATE PRODUK APOTEK GAGAL")


	return render(request, 'update/update_produk_apotek.html', context)


def delete_produk_apotek(request):
	"""
	function untuk menghapus data produk apotek pada baris yang diminta.
	"""
	id_produk = request.POST["id_produk"]
	id_apotek = request.POST["id_apotek"]

	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")
	cursor.execute(
        f"""
		DELETE FROM list_produk_dibeli
		WHERE id_apotek = '{id_apotek}'
		AND id_produk = '{id_produk}';

		DELETE FROM produk_apotek
		WHERE id_produk = '{id_produk}'
		AND id_apotek = '{id_apotek}';
		"""
    )

	return redirect('/produk-apotek/tabel/')


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


def __update(id_produk, id_apotek, harga_jual, satuan_penjualan, stok):
	"""
	function untuk memperbarui data produk apotek.
	"""
	cursor = connection.cursor()
	cursor.execute("SET SEARCH_PATH TO farmakami;")
	cursor.execute(
		f"""
		UPDATE list_produk_dibeli
		SET (id_produk, id_apotek) = ('{id_produk}', '{id_apotek}')
		WHERE id_produk = '{id_produk}' and id_apotek = '{id_apotek}';
	
		UPDATE produk_apotek
		SET (id_produk, id_apotek, harga_jual, satuan_penjualan, stok) = 
		('{id_produk}', '{id_apotek}', '{harga_jual}', '{satuan_penjualan}', '{stok}')
		WHERE id_produk = '{id_produk}' and id_apotek = '{id_apotek}';
		"""
	)


def __fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
