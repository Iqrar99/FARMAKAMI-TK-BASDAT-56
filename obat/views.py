from django.shortcuts import render, redirect
from django.db import connection
from .forms import CreateObatForm, UpdateObatForm

def tabel_obat(request):
    if 'email' not in request.session:
        return redirect('/login/')

    query = """SELECT * FROM obat;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_obat = __fetch(cursor)

    context = {
        'data_obat': data_obat,
        'role': request.session['role']
    }
    
    return render(request, 'tabel/read_obat.html', context)


def buat_obat(request):
    if 'email' not in request.session:
        return redirect('/login/')

    if (request.session['role'] == 'kurir'):
        return redirect(f'/navigate/{request.session["role"]}/')
    elif (request.session['role'] == 'konsumen'):
        return redirect(f'/navigate/{request.session["role"]}/')

    form = CreateObatForm(request.POST or None)
    context = {
        'form': form,
        'error': [],
        'role': request.session['role'],
    }

    if (request.method == 'POST' and form.is_valid()):
        valid = True
        print(request.POST)

        id_merk_obat = request.POST['id_merk_obat']
        netto = request.POST['netto_obat']
        dosis = request.POST['dosis_obat']
        aturan_pakai = request.POST['aturan_pakai']
        kontraindikasi = request.POST['kontraindikasi']
        bentuk_kesediaan = request.POST['bentuk_kesediaan']

        aturan_pakai = "NULL" if aturan_pakai == '' else "'"+aturan_pakai+"'"
        kontraindikasi = "NULL" if kontraindikasi == '' else "'"+kontraindikasi+"'"

        new_id_produk = __create_id_produk()

        try:
            __create_obat(new_id_produk, id_merk_obat, netto, dosis,
                          aturan_pakai, kontraindikasi, bentuk_kesediaan)
            print("SUKSES MENGINPUT OBAT")

            return redirect('/obat/tabel/')

        except:
            print("GAGAL MENGINPUT OBAT")

    return render(request, 'create/create_obat.html', context)


def update_obat(request, id):
    if 'email' not in request.session:
        return redirect('/login/')

    if (request.session['role'] == 'kurir'):
        return redirect(f'/navigate/{request.session["role"]}/')
    elif (request.session['role'] == 'konsumen'):
        return redirect(f'/navigate/{request.session["role"]}/')

    # Panggil data target untuk dijadikan initial di formnya
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(f"SELECT * FROM obat WHERE id_obat = '{id}';")

    data_obat = __fetch(cursor)[0]

    data_id_obat = data_obat['id_obat']
    data_id_merk = data_obat['id_merk_obat']
    data_id_produk = data_obat['id_produk']
    data_netto = data_obat['netto']
    data_dosis = data_obat['dosis']
    data_aturan = data_obat['aturan_pakai']
    data_kontraindikasi = data_obat['kontraindikasi']
    data_kesediaan = data_obat['bentuk_kesediaan']

    form = UpdateObatForm(request.POST or None, initial={
        'id_obat' : data_id_obat,
        'id_produk' : data_id_produk,
        'id_merk_obat' : data_id_merk,
        'netto_obat' : data_netto,
        'dosis_obat' : data_dosis,
        'aturan_pakai' : data_aturan,
        'kontraindikasi' : data_kontraindikasi,
        'bentuk_kesediaan' : data_kesediaan,
    })

    context = {
        'error': [],
        'form' : form,
    }

    if (request.method == 'POST' and form.is_valid()):
        print(request.POST)

        # hacking the data since it cannot pass the POST request
        # from disabled input
        id_obat = data_id_obat
        id_produk = data_id_produk

        id_merk = request.POST['id_merk_obat']
        netto = request.POST['netto_obat']
        dosis = request.POST['dosis_obat']
        aturan = request.POST['aturan_pakai']
        kontraindikasi = request.POST['kontraindikasi']
        kesediaan = request.POST['bentuk_kesediaan']

        aturan = "NULL" if aturan == '' else "'"+aturan+"'"
        kontraindikasi = "NULL" if kontraindikasi == '' else "'"+kontraindikasi+"'"

        try:
            __update(id_obat, id_produk, id_merk, netto, dosis, aturan, kontraindikasi, kesediaan)
            print("SUKSES UPDATE")

            return redirect("/obat/tabel/")

        except:
            print("GAGAL UPDATE")

    return render(request, 'update/update_obat.html', context)


def delete_obat(request):
    """
    function untuk menghapus data obat pada baris yang diminta.
    """
    id_target = request.POST["id_target"]

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        DELETE FROM obat
        WHERE id_obat = '{id_target}';
        """
    )

    return redirect('/obat/tabel/')


def __create_obat(id_produk, id_merk, netto, dosis, aturan, kontraindikasi, bentuk_kesediaan):
    """
    function untuk membuat data obat yang baru.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    # generate id obat
    cursor.execute(
        """
        SELECT id_obat FROM obat
        ORDER BY id_obat DESC
        LIMIT 1;
        """
    )
    latest_id = int(__fetch(cursor)[0]['id_obat'][-2:])
    new_id = latest_id + 1
    if new_id < 10:
        new_id = 'O0' + str(new_id)
    else:
        new_id = 'O' + str(new_id)

    cursor.execute(
        f"""
        INSERT INTO obat
        VALUES ('{new_id}', '{id_produk}', '{id_merk}', '{netto}', '{dosis}',
        {aturan}, {kontraindikasi}, '{bentuk_kesediaan}');
        """
    )

def __create_id_produk() -> str:
    """
    function untuk membuat id produk yang baru.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    cursor.execute(
        """
        SELECT id_produk FROM produk
        ORDER BY id_produk DESC
        LIMIT 1;
        """
    )
    latest_id = int(__fetch(cursor)[0]['id_produk'][-3:])
    new_id = latest_id + 1
    if new_id < 10:
        new_id = 'PR00' + str(new_id)
    elif new_id < 100:
        new_id = 'PR0' + str(new_id)
    else:
        new_id = 'PR' + str(new_id)

    cursor.execute(f"INSERT INTO produk VALUES ('{new_id}');")

    print('PRODUK BARU BERHASIL DIINPUT')
    return new_id


def __update(id_obat, id_produk, id_merk, netto, dosis, aturan, kontraindikasi, bentuk_kesediaan):
    """
    function untuk memperbarui data obat.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    cursor.execute(
        f"""
        UPDATE obat
        SET (id_merk_obat, netto, dosis, aturan_pakai, kontraindikasi, bentuk_kesediaan) =
        ('{id_merk}', '{netto}', '{dosis}', {aturan}, {kontraindikasi}, '{bentuk_kesediaan}')
        WHERE id_obat = '{id_obat}' AND id_produk = '{id_produk}';
        """
    )

def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
