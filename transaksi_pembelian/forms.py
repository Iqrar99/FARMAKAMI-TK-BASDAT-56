from django import forms
from django.db import connection

class TransaksiPembelianForm(forms.Form):
    def get_id_konsumen():
        """
        function untuk mendapatkan id yang tersedia pada tabel apotek
        """
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_konsumen FROM konsumen;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            number = int(data['id_konsumen'][-2:])
            packed_data.append((data['id_konsumen'], data['id_konsumen']))

        return tuple(packed_data)
    
    id_konsumen = forms.ChoiceField(
        label='ID Konsumen',
        choices=get_id_konsumen()
    )

class UpdateTransaksiPembelian(forms.Form):
    id_transaksi = forms.CharField(
        label='ID Transaksi',
        max_length=10,
        required=True,
        disabled=True,
    )

    waktu_pembelian = forms.CharField(
        label='Waktu Pembelian', disabled=True, initial='2020-04-17 17:20:20')

    total_pembayaran = forms.CharField(
        label='total_pembayaran',
        max_length=50,
        required=True,
        disabled=True,
    )
    
    #TO BE CHANGED
    id_konsumen = forms.CharField(
        label='ID Konsumen', widget=forms.Select(choices=((1,1))))
