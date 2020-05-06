from django import forms

class BalaiPengobatanForm(forms.Form):
    alamat_balai = forms.CharField(
        label='Alamat Balai',
        max_length=200,
        required=True
    )
    nama_balai = forms.CharField(
        label='Nama Balai',
        max_length=50,
    )
    jenis_balai = forms.CharField(
        label='Jenis Balai',
        max_length=30,
        required=True
    )
    telepon_balai = forms.CharField(
        label='Telepon Balai',
        max_length=20,
        required=True
    )
