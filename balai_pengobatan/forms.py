from django import forms
from django.db import connection

class Get(object):
    def __init__(self):
        super().__init__()

    def get_id_apotek_berasosiasi(self):
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

class CreateBalaiPengobatanForm(forms.Form):
    g = Get()    

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
        choices = g.get_id_apotek_berasosiasi()
    )

class UpdateBalaiPengobatanForm(forms.Form):
    g = Get()

    id_balai = forms.CharField(
        label='ID Balai',
        disabled=True
    )
    alamat_balai = forms.CharField(
        label='Alamat Balai',
        max_length=200,
    )
    nama_balai = forms.CharField(
        label='Nama Balai',
        max_length=50,
    )
    jenis_balai = forms.CharField(
        label='Jenis Balai',
        max_length=30,
    )
    telepon_balai = forms.CharField(
        label='Telepon Balai',
        max_length=20,
    )
    id_apotek = forms.ChoiceField(
        label='Daftar ID Apotek berasosiasi',
        choices=g.get_id_apotek_berasosiasi()
    )



