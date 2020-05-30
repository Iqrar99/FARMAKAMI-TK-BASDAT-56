from django import forms
from django.db import connection

class TransaksiPembelianForm(forms.Form):
    def get_id_konsumen():
        """
        function untuk mendapatkan id yang tersedia pada tabel transaksi pembelian
        """
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_konsumen FROM konsumen;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            packed_data.append((data['id_konsumen'], data['id_konsumen']))

        return tuple(packed_data)

    id_konsumen = forms.ChoiceField(
        label='ID Konsumen',
        choices=get_id_konsumen()
    )

class UpdateTransaksiPembelian(forms.Form):
    def get_id_konsumen():
        """
        function untuk mendapatkan id yang tersedia pada tabel transaksi pembelian
        """
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_konsumen FROM konsumen;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            packed_data.append((data['id_konsumen'], data['id_konsumen']))

        return tuple(packed_data)

    id_transaksi = forms.CharField(
        label='ID Transaksi',
        max_length=10,
        disabled=True,
    )

    waktu_pembelian = forms.CharField(
        label='Waktu Pembelian', disabled=True, max_length=50)

    total_pembayaran = forms.CharField(
        label='Total Pembayaran',
        max_length=50,
        disabled=True,
    )

    id_konsumen = forms.ChoiceField(
        label='ID Konsumen',
        choices=get_id_konsumen()
    )
