from django import forms
from django.db import connection

class Get(object):
    def __init__(self):
        super().__init__()

    def get_id_produk(self):
        """
        function untuk mendapatkan id produk pada tabel produk.
        """
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

    def get_id_apotek(self):
        """
        function untuk mendapatkan id apotek pada tabel apotek.
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


class CreateProdukApotekForm(forms.Form):
    g = Get()

    id_produk = forms.ChoiceField(
        label='ID Produk',
        choices=g.get_id_produk()
    )
    id_apotek = forms.ChoiceField(
        label='ID Apotek',
        choices=g.get_id_apotek()
    )
    harga_jual = forms.IntegerField(label='Harga Jual')
    satuan_penjualan = forms.CharField(
        label='Satuan Penjualan',
        max_length=5,
        required=True
    )  
    stok = forms.IntegerField(label='Stok')


class UpdateProdukApotekForm(forms.Form):
    g = Get()

    id_produk = forms.ChoiceField(
        label='ID Produk',
        choices=g.get_id_produk()
    )
    id_apotek = forms.ChoiceField(
        label='ID Apotek',
        choices=g.get_id_apotek()
    )
    harga_jual = forms.IntegerField(label='Harga Jual')
    satuan_penjualan = forms.CharField(
        label='Satuan Penjualan',
        max_length=5,
        required=True
    )  
    stok = forms.IntegerField(label='Stok')
    
