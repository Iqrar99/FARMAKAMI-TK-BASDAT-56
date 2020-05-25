from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import connection
from django.shortcuts import render, reverse, redirect
from .forms import AdminForm, ConsumerForm, KurirForm, CSForm
from .registration import Registration


def main_menu_register(request):
    context = {
        'register_admin' : reverse('register_admin'),
        'register_consumer' : reverse('register_consumer'),
        'register_kurir' : reverse('register_kurir'),
        'register_cs' : reverse('register_cs'),
    }

    return render(request, 'register.html', context)

def register_admin(request):
    """
    function untuk mendaftarkan admin.
    """
    if 'email' in request.session:
        return redirect('/user-profile/')

    form = AdminForm(request.POST or None)
    context = {
        'form' : form,
        'error' : []
    }

    if (request.method == 'POST' and form.is_valid()):
        valid = True
        
        # validasi email
        email = request.POST['email']
        if check_email(email):
            valid = valid and False
            context['error'].append('The email has been registered before.')

        nama_lengkap = request.POST['nama_lengkap']
        
        # validasi password
        try:
            password = request.POST['password']
            validate_password(password)

        except ValidationError as error:
            context['error'].extend(
                list(map(lambda msg: msg.replace("This", "The"), error)))
            valid = valid and False

        # validasi nomor telepon
        no_telp = request.POST['no_telp']
        if not no_telp.isnumeric():
            context['error'].append(
                'The phone number should contains number only.')
            valid = valid and False

        context['registered'] = ""
        if valid:
            reg = Registration()

            try:
                reg.register_admin(
                    email, password = password, nama = nama_lengkap, telp = no_telp)
                context['registered'] = "New user has been registered."
            except:
                print('REGISTRASI GAGAL')

    return render(request, 'register_admin.html', context)


def register_consumer(request):
    context = {
        'form' : ConsumerForm(request.POST or None)
    }

    return render(request, 'register_consumer.html', context)


def register_kurir(request):
    """
    function untuk mendaftarkan kurir.
    """
    if 'email' in request.session:
        return redirect('/user-profile/')

    form = KurirForm(request.POST or None)
    context = {
        'form': form,
        'error': []
    }

    if (request.method == 'POST' and form.is_valid()):
        valid = True

        nama_lengkap = request.POST['kurir_full_name']
        nama_perusahaan = request.POST['kurir_company_name']

        # validasi email
        email = request.POST['kurir_email']
        if check_email(email):
            valid = valid and False
            context['error'].append('The email has been registered before.')

        # validasi password
        try:
            password = request.POST['kurir_password']
            validate_password(password)

        except ValidationError as error:
            context['error'].extend(
                list(map(lambda msg: msg.replace("This", "The"), error)))
            valid = valid and False

        # validasi nomor telepon
        no_telp = request.POST['kurir_telp']
        if not no_telp.isnumeric():
            context['error'].append(
                'The phone number should contains number only.')
            valid = valid and False

        context['registered'] = ""
        if valid:
            reg = Registration()

            try:
                reg.register_kurir(
                    email,
                    nama_perusahaan,
                    password = password,
                    nama = nama_lengkap,
                    telp = no_telp
                )
                context['registered'] = "New user has been registered."
            except:
                print('REGISTRASI GAGAL')


    return render(request, 'register_kurir.html', context)


def register_cs(request):
    context = {
        'form' : CSForm(request.POST or None)
    }

    return render(request, 'register_cs.html', context)

def check_email(email:str) -> bool:
    """
    function untuk memvalidasi apakah email pernah terdaftar atau belum.
    """
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO farmakami;")
    cursor.execute(f"SELECT email FROM pengguna WHERE email = '{email}';")

    columns = [col[0] for col in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]

    if len(result) == 0:
        print("EMAIL BELUM TERDAFTAR")
        return False
    
    print("EMAIL SUDAH TERDAFTAR")
    return True
