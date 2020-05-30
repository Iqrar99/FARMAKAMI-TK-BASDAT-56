from datetime import datetime
from django import forms
from django.db import connection

class PengantaranForm(forms.Form):
    def get_id_transaksi():
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_transaksi_pembelian FROM transaksi_pembelian;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            packed_data.append((data['id_transaksi_pembelian'], data['id_transaksi_pembelian']))

        return tuple(packed_data)

    id_transaksi = forms.ChoiceField(
        label='ID Transaksi',
        choices=get_id_transaksi()
    )
    waktu = forms.DateTimeField(
        initial=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        label='Waktu',  
    )
    biaya_kirim = forms.IntegerField(
        label='Biaya Kirim',
    )

class UpdatePengantaranForm(forms.Form):
    def get_id_transaksi():
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_transaksi_pembelian FROM transaksi_pembelian;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            packed_data.append((data['id_transaksi_pembelian'], data['id_transaksi_pembelian']))

        return tuple(packed_data)

    def get_id_kurir():
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_kurir FROM kurir;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            packed_data.append((data['id_kurir'], data['id_kurir']))

        return tuple(packed_data)


    id_pengantaran = forms.CharField(
    label='ID Pengantaran',
    disabled=True,
)
    id_kurir = forms.ChoiceField(
    label='ID Kurir',
    choices= get_id_kurir(),
)
    id_transaksi = forms.ChoiceField(
    label='ID Transaksi',
    choices= get_id_transaksi(),
)
    waktu = forms.CharField(
    label='Waktu',
    max_length=50,
)
    status_pengiriman = forms.CharField(
    label='Status',
    max_length=50,
)
    biaya_kirim = forms.CharField(
    label='Biaya_kirim',
    max_length=50,
)
    total_biaya = forms.CharField(
    label='Total_biaya',
    disabled=True,
)
