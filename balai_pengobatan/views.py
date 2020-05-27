from django.shortcuts import render, redirect
from django.db import connection
from .forms import CreateBalaiPengobatanForm, UpdateBalaiPengobatanForm

def tabel_balai_pengobatan(request):
    if 'email' not in request.session:
        return redirect('/login/')

    query = """SELECT * FROM balai_pengobatan;"""

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_balai = __fetch(cursor)

    context = {
        'data_balai': data_balai,
        'role': request.session['role']
    }

    return render(request, 'tabel/read_balai_pengobatan.html', context)


def buat_balai_pengobatan(request):
    if 'email' not in request.session:
        return redirect('/login/')

    if request.session['role'] != 'admin-apotek':
        return redirect(f'/navigate/{request.session["role"]}/')

    form = CreateBalaiPengobatanForm(request.POST or None)
    context = {
        'form': form,
        'error': []
    }

    if (request.method == 'POST' and form.is_valid()):
        valid = True
        print(request.POST)

        # validasi alamat
        alamat = request.POST['alamat_balai']
        if __check_alamat(alamat):
            valid = valid and False
            context['error'].append('The address has been registered before.')

        nama_balai = request.POST['nama_balai']
        jenis = request.POST['jenis_balai']
        id_apotek = request.POST['id_apotek']

        # validasi nomor telepon
        telp = request.POST['telepon_balai']
        if (telp != '' and (not telp.isnumeric())):
            context['error'].append(
                'The phone number should contains number only.')
            valid = valid and False

        if valid:
            try:
                __create(alamat, nama_balai, jenis, telp, id_apotek)

                print('SUKSES MEMBUAT')
                return redirect('/balai-pengobatan/tabel/')
            except:
                print('GAGAL MEMBUAT')

    return render(request, 'create/create_balai_pengobatan.html', context)

def update_balai_pengobatan(request):
    context = {
        'form': UpdateBalaiPengobatanForm(request.POST or None)
    }

    return render(request, 'update/update_balai_pengobatan.html', context)

def delete_balai(request):
    """
    function untuk menghapus data balai pengobatan.
    """
    id_balai = request.POST['id_balai']

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        DELETE FROM balai_apotek
        WHERE id_balai = '{id_balai}';
        
        DELETE FROM balai_pengobatan
        WHERE id_balai = '{id_balai}';
        """
    )

    return redirect('/balai-pengobatan/tabel/')

def __check_alamat(alamat: str):
    """
    function untuk memvalidasi apakah alamat pernah terdaftar atau belum.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(
        f"""
        SELECT alamat_balai FROM balai_pengobatan
        WHERE alamat_balai = '{alamat}';
        """
    )

    result = __fetch(cursor)

    if len(result) == 0:
        print("ALAMAT BELUM TERDAFTAR")
        return False

    print("ALAMAT SUDAH TERDAFTAR")
    return True

def __create(alamat, nama_balai, jenis, telp, id_apotek):
    """
    function untuk memasukkan input ke dalam tabel BALAI_PENGOBATAN
    dan tabel BALAI_APOTEK.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")

    # generate id balai
    cursor.execute(
        """
    SELECT id_balai FROM balai_pengobatan
    ORDER BY id_balai DESC
    LIMIT 1;
    """
    )
    latest_id = int(__fetch(cursor)[0]['id_balai'][-2:])
    new_id = latest_id + 1
    if new_id < 10:
        new_id = 'BA0' + str(new_id)
    else:
        new_id = 'BA' + str(new_id)

    telp = "NULL" if telp == '' else "'"+telp+"'"

    # balai pengobatan
    query = f"""
    INSERT INTO balai_pengobatan
    VALUES ('{new_id}', '{alamat}', '{nama_balai}', '{jenis}', {telp});
    """
    cursor.execute(query)

    # balai apotek
    query = f"""
    INSERT INTO balai_apotek
    VALUES ('{new_id}', '{id_apotek}');
    """
    cursor.execute(query)

def __fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
