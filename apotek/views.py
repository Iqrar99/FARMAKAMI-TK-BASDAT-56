from django.shortcuts import render, redirect
from django.db import connection
from .forms import CreateApotekForm, UpdateApotekForm
import time


def tabel_apotek(request):
    """
    function untuk menampilkan data apotek.
    """
    if 'email' not in request.session:
        return redirect('/login/')

    query = """SELECT * FROM apotek;"""
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)
    data_apotek = __fetch(cursor)

    context = {
        'data_apotek': data_apotek,
        'role': request.session['role']
    }

    return render(request, 'tabel/read_apotek.html', context)


def buat_apotek(request):
    """
    function untuk membuat data apotek.
    """
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
                __create_apotek(email, no_sia, nama_penyelenggara,
                                nama_apotek, alamat, telp)
                print("APOTEK SUKSES DIBUAT")
                return redirect('/apotek/tabel/')

            except:
                print("APOTEK GAGAL DIBUAT")

    return render(request, 'create/create_apotek.html', context)


def update_apotek(request, id):
    if 'email' not in request.session:
        return redirect('/login/')

    if (request.session['role'] != 'admin-apotek'):
        return redirect(f'/navigate/{request.session["role"]}/')

    # Panggil data initial pada form
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(f"SELECT * FROM apotek")

    data_apotek = {}
    x = __fetch(cursor)
    for i in range(len(x)):
        if x[i]['id_apotek'] == id:
            data_apotek = x[i]
            break

    data_nama_apotek = data_apotek['nama_apotek']
    data_alamat_apotek = data_apotek['alamat_apotek']
    data_telepon_apotek = data_apotek['telepon_apotek']
    data_nama_penyelenggara = data_apotek['nama_penyelenggara']
    data_no_sia = data_apotek['no_sia']
    data_email = data_apotek['email']

    form = UpdateApotekForm(request.POST or None, initial = {
        'id_apotek' : id,
        'nama_apotek': data_nama_apotek,
        'alamat_apotek' : data_alamat_apotek,
        'telepon_apotek' : data_telepon_apotek,
        'nama_penyelenggara': data_nama_penyelenggara,
        'no_sia' : data_no_sia,
        'email_penyelenggara' : data_email
    })

    context = {
        'error': [],
        'form': form,
    }


    if (request.method == 'POST' and form.is_valid()):
        valid = True

        id_apotek = id
        nama_apotek = request.POST['nama_apotek']
        alamat_apotek = request.POST['alamat_apotek']
        telepon_apotek = request.POST['telepon_apotek']
        nama_penyelenggara = request.POST['nama_penyelenggara']
        no_sia = request.POST['no_sia']
        email_penyelenggara = request.POST['email_penyelenggara']
        

        # validasi no telp
        if not telepon_apotek.isnumeric():
            context['error'].append(
                'The phone number should contains number only.')
            valid = valid and False

        # validasi no SIA
        if not no_sia.isnumeric():
            context['error'].append(
                'The SIA number should contains number only.')
            valid = valid and False

        if valid:

            try:
                __update(id_apotek, nama_apotek, alamat_apotek, 
                    telepon_apotek, nama_penyelenggara, no_sia, email_penyelenggara)
                print("UPDATE APOTEK SUKSES")
                return redirect('/apotek/tabel/')

            except:
                print("UPDATE APOTEK GAGAL")


    return render(request, 'update/update_apotek.html', context)


def delete_apotek(request):
    """
    function untuk menghapus data apotek.
    """
    id_apotek = request.POST['id_apotek']
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        DELETE FROM list_produk_dibeli
        WHERE id_apotek = '{id_apotek} ';

        DELETE FROM produk_apotek
        WHERE id_apotek = '{id_apotek}';

        DELETE FROM balai_apotek
        WHERE id_apotek = '{id_apotek}';

        UPDATE admin_apotek
        SET id_apotek = NULL
        WHERE id_apotek = '{id_apotek}';

        DELETE FROM apotek
        WHERE id_apotek = '{id_apotek}';
        """
    )

    time.sleep(10)
    return redirect('apotek/tabel/')


def __create_apotek(email, no_sia, nama_penyelenggara, nama_apotek, alamat, telp):
    """
    function untuk menambahkan apotek ke database.
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


def __update(id_apotek, nama_apotek, alamat_apotek, telepon_apotek, nama_penyelenggara, no_sia, email_penyelenggara):
    """
    function untuk memperbarui data apotek.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        UPDATE apotek
        SET (nama_apotek, alamat_apotek, telepon_apotek, nama_penyelenggara, no_sia, email) = 
        ('{nama_apotek}', '{alamat_apotek}', '{telepon_apotek}', '{nama_penyelenggara}', '{no_sia}', '{email_penyelenggara}')
        WHERE id_apotek = '{id_apotek}';
        """
    )


def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
