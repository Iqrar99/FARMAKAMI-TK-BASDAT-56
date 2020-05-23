from django.shortcuts import render, redirect
from django.db import connection
from .forms import LoginForm

# ----------- LOGIN -----------
def user_login(request):
    """
    function yang bertanggung jawab dalam user login.
    """
    
    if 'email' in request.session:
        return redirect(f"/navigate/{request.session['role']}")

    response = {}

    form = LoginForm(request.POST or None)
    if (request.method == 'POST' and form.is_valid()):
        response['email'] = request.POST['email']
        response['password'] = request.POST['password']
        response['invalid'] = False

        registered = is_registered(response['email'], response['password'])
        if not registered:
            response['invalid'] = True

        else:
            role = role_check(response['email'])
            if role == None:
                response['invalid'] = True

            else:
                request.session['role'] = role
                request.session['email'] = response['email']
                request.session['nama'] = get_name(response['email'])

                return redirect(f'/navigate/{role}')

    response['form'] = form

    return render(request, 'login.html', context = response)

def is_registered(email:str, password:str) -> bool:
    """
    function untuk cek apakah user sudah terdaftar sebelumnya.
    """
    query = "SELECT * FROM pengguna;"

    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    data_pengguna = fetch(cursor)

    for data in data_pengguna:
        if data['email'] == email and data['password'] == password:
            return True
    
    return False

def role_check(email:str):
    """
    function untuk cek role dari email yang diduga telah terdaftar.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    
    # cek kurir
    cursor.execute("SELECT email FROM kurir;")
    data_kurir = fetch(cursor)
    for data in data_kurir:
        if data['email'] == email:
            return 'kurir'
    
    # cek cs
    cursor.execute("SELECT email FROM cs;")
    data_cs = fetch(cursor)
    for data in data_cs:
        if data['email'] == email:
            return 'cs'

    # cek admin
    cursor.execute("SELECT email FROM admin_apotek;")
    data_cs = fetch(cursor)
    for data in data_cs:
        if data['email'] == email:
            return 'admin-apotek'

    # cek konsumen
    cursor.execute("SELECT email FROM konsumen;")
    data_cs = fetch(cursor)
    for data in data_cs:
        if data['email'] == email:
            return 'konsumen'

    return None

def get_name(email:str) -> str:
    """
    function untuk mendapatkan nama user yang login.
    """
    query = f"""
    SELECT nama_lengkap AS nama
    FROM pengguna
    WHERE email = '{email}';
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    result = fetch(cursor)

    return result[0]['nama']

def fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
