from django.shortcuts import render, redirect
from django.db import connection
from .forms import ListProdukForm, UpdateList

# Create your views here.
def tabel_list_produk_dibeli(request):
    if 'email' not in request.session:
        return redirect('/login/')

    query = """SELECT * FROM list_produk_dibeli;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_list_produk = __fetch(cursor)

    context = {
        'data_list_produk': data_list_produk,
        'role': request.session['role']
    }

    return render(request, 'tabel/read_list_produk_dibeli.html', context)

def create_list_produk_dibeli(request):
    if 'email' not in request.session:
        return redirect('/login/')

    if request.session['role'] != 'admin-apotek':
        return redirect(f'/navigate/{request.session["role"]}/')

    form = ListProdukForm(request.POST or None)
    context = {
        'form': form,
        'error': []
    }
    
    if (request.method == 'POST' and form.is_valid()):
        valid = True

        id_produk = request.POST['id_produk']
        id_apotek = request.POST['id_apotek']
        id_transaksi = request.POST['id_transaksi']

        # validasi jumlah
        jumlah = request.POST['jumlah']
        if int(jumlah) < 0:
            valid = valid and False
            context['error'].append('Jumlah can not be negative.')

        if valid:
            try:
                __create_produk_dibeli(jumlah, id_apotek, id_produk, id_transaksi)
                print("SUKSES MENGINPUT PRODUK DIBELI")

                return redirect('/list-produk-dibeli/tabel/')

            except:
                print("GAGAL PRODUK DIBELI")

    return render(request, 'create/create_list_produk_dibeli.html', context)

def update_list_produk_dibeli(request):
	context = {
        'form' : UpdateList(request.POST or None)
    }
	return render(request, 'update/update_list_product_dibeli.html', context)

def __create_produk_dibeli(jumlah, id_apotek, id_produk, id_transaksi):
    """
    function untuk menginput data produk yang dibeli.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    cursor.execute(
        f"""
        INSERT INTO list_produk_dibeli
        VALUES ({jumlah}, '{id_apotek}', '{id_produk}', '{id_transaksi}');
        """
    )

def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
