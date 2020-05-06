from django import forms

class ApotekForm(forms.Form):
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