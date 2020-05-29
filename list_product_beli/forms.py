from django import forms
from django.db import connection


class ListProdukForm(forms.Form):
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

    def get_id_transaksi():
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_transaksi_pembelian FROM transaksi_pembelian;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            number = int(data['id_transaksi_pembelian'][-3:])
            packed_data.append((data['id_transaksi_pembelian'], data['id_transaksi_pembelian']))

        return tuple(packed_data)

    id_produk = forms.ChoiceField(
        label='ID Produk',
        choices=get_id_produk()
    )
    id_apotek = forms.ChoiceField(
        label='ID Apotek',
        choices=get_id_apotek()
    )
    id_transaksi = forms.ChoiceField(
        label='ID Transaksi',
        choices=get_id_transaksi()
    )
    jumlah = forms.IntegerField(
        label='jumlah',
    )

class UpdateList(forms.Form):
    def get_id_transaksi():
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_transaksi_pembelian FROM transaksi_pembelian;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            number = int(data['id_transaksi_pembelian'][-3:])
            packed_data.append((data['id_transaksi_pembelian'], data['id_transaksi_pembelian']))

        return tuple(packed_data)

    id_produk = forms.CharField(
        label='ID Produk',
        disabled=True,
    )
    id_apotek = forms.CharField(
        label='ID Apotek',
        disabled=True,
    )
    id_transaksi_pembelian = forms.ChoiceField(
        label='ID Transaksi Pembelian',
        choices= get_id_transaksi(),
    )   
    jumlah = forms.CharField(
        label='jumlah',
        max_length=50,
    )
