from django import forms

class CreateBalaiPengobatanForm(forms.Form):
    alamat_balai = forms.CharField(
        label='Alamat Balai',
        max_length=200,
        required=True
    )
    nama_balai = forms.CharField(
        label='Nama Balai',
        max_length=50,
        required=True
    )
    jenis_balai = forms.CharField(
        label='Jenis Balai',
        max_length=30,
        required=True
    )
    telepon_balai = forms.CharField(
        label='Telepon Balai',
        max_length=20,
    )


class UpdateBalaiPengobatanForm(forms.Form):
    id_balai = forms.CharField(
        label='ID Balai',
        disabled=True
    )
    alamat_balai = forms.CharField(
        label='Alamat Balai',
        max_length=200,
        required=True
    )
    nama_balai = forms.CharField(
        label='Nama Balai',
        max_length=50,
        required=True
    )
    jenis_balai = forms.CharField(
        label='Jenis Balai',
        max_length=30,
        required=True
    )
    telepon_balai = forms.CharField(
        label='Telepon Balai',
        max_length=20,
    )
    id_merk_obat = forms.ChoiceField(
        label='Daftar ID Apotek berasosiasi',
        choices=(
            (1, 1),
            (2, 2)
        )
    )
