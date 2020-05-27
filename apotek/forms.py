from django import forms

class CreateApotekForm(forms.Form):
    email_penyelenggara = forms.EmailField(
        label='Email Penyelenggara'
    )
    no_sia = forms.CharField(
        label='No SIA Penyelenggara',
        max_length=20,
    )
    nama_penyelenggara = forms.CharField(
        label='Nama Penyelenggara',
        max_length=50,
    )
    nama_apotek = forms.CharField(
        label='Nama Apotek',
        max_length=50,
    )
    alamat_apotek = forms.CharField(
        label='Alamat Apotek',
        max_length=200,
    )  
    telepon_apotek = forms.CharField(
        label='No telp. Apotek',
        max_length=20
    )

class UpdateApotekForm(forms.Form):
    id_apotek = forms.CharField(
        label='ID Apotek',
        max_length=10,
        required=True,
        disabled=True
    )
    nama_apotek = forms.CharField(
        label='Nama Apotek',
        max_length=50,
        required=True
    )
    alamat_apotek = forms.CharField(
        label='Alamat Apotek',
        max_length=200,
        required=True
    )  
    telepon_apotek = forms.CharField(
        label='No telp Apotek',
        max_length=20
    )
    nama_penyelenggara = forms.CharField(
        label='Nama Penyelenggara',
        max_length=50,
        required=True
    )
    no_sia = forms.CharField(
        label='No SIA Penyelenggara',
        max_length=20,
        required=True
    )
    email_penyelenggara = forms.CharField(
        label='Email Penyelenggara',
        max_length=50,
        required=True
    )

