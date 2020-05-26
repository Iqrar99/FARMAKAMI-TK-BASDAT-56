from django import forms
from django.db import connection

class CreateProdukApotekForm(forms.Form):
    def get_id_produk():
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_produk FROM produk;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            number = int(data['id_produk'][-3:])
            packed_data.append((data['id_produk'], data['id_produk']))

        return tuple(packed_data)

    def get_id_apotek():
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

    id_produk = forms.ChoiceField(
        label='ID Produk',
        choices=get_id_produk()
    )
    id_apotek = forms.ChoiceField(
        label='ID Apotek',
        choices=get_id_apotek()
    )
    harga_jual = forms.IntegerField(label='Harga Jual')
    satuan_penjualan = forms.CharField(
        label='Satuan Penjualan',
        max_length=5,
        required=True
    )  
    stok = forms.IntegerField(label='Stok')

class UpdateProdukApotekForm(forms.Form):
    id_produk = forms.CharField(
        label='ID Produk',
        widget=forms.Select(choices=((1,1)))
    )
    id_apotek = forms.CharField(
        label='ID Apotek',
        widget=forms.Select(choices=((1,1)))
    )
    harga_jual = forms.CharField(
        label='Harga Jual',
        max_length=15,
        required=True
    )
    satuan_penjualan = forms.CharField(
        label='Satuan Penjualan',
        max_length=5,
        required=True
    )  
    stok = forms.CharField(
        label='Stok',
        max_length=10,
        required=True
    )
    
