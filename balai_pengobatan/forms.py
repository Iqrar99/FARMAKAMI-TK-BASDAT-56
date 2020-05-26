from django import forms
from django.db import connection

class CreateBalaiPengobatanForm(forms.Form):
    def get_id_apotek_berasosiasi():
        """
        function untuk mendapatkan id yang tersedia pada tabel apotek
        """
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_apotek FROM apotek;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            number = int(data['id_apotek'][-2:])
            packed_data.append((data['id_apotek'], data['id_apotek']))

        return tuple(packed_data)

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
        required=False
    )
    id_apotek = forms.ChoiceField(
        label = 'Daftar ID Apotek berasosiasi' ,
        choices = get_id_apotek_berasosiasi()
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



