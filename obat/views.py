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

    if request.session['role'] != 'admin-apotek':
        return redirect(f'/navigate/{request.session["role"]}/')

    form = CreateObatForm(request.POST or None)
    context = {
        'form': form,
        'error': []
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

def update_obat(request):
    context = {
        'form' : UpdateObatForm(request.POST or None)
    }

    return render(request, 'update/update_obat.html', context)

def delete_obat(request):
    id_target = request.POST["id_target"]
    print(id_target)

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


def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
