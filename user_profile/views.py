from django.shortcuts import render, redirect
from django.db import connection

def user_profile(request):
    if 'email' not in request.session:
        return redirect('/login/')

    email = request.session['email']
    role = request.session['role']

    role_display = {
        'admin-apotek' : 'Admin Apotek',
        'kurir' : 'Kurir',
        'cs' : 'Customer Service',
        'konsumen' : 'Konsumen',
    }

    context = {
        'role' : role_display[role],
        'nama' : request.session['nama'],
        'email' : email,
        'telepon' : get_telepon(email),
        'navigate' : f'/navigate/{role}'
    }

    return render(request, 'user_profile.html', context)

def get_telepon(email:str) -> str:
    """
    function untuk mendapatkan telepon user berdasarkan email.
    """

    query = f"""
    SELECT telepon FROM pengguna
    WHERE email = '{email}'; 
    """
    
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(query)

    result = fetch(cursor)

    return result[0]['telepon']

def fetch(cursor):
	columns = [col[0] for col in cursor.description]
	return [dict(zip(columns, row)) for row in cursor.fetchall()]
