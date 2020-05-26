from django import forms
from django.db import connection

ID_T0 = [
    ('T001', 'T001'),
    ('T002', 'T002'),
    ('T003', 'T003'),
    ('T004', 'T004'),
    ('T005', 'T005'),
    ('T006', 'T006'),
    ('T007', 'T007'),
    ('T008', 'T008'),
    ('T009', 'T009'),
    ('T010', 'T010'),
    ('T011', 'T011'),
    ('T012', 'T012'),
    ('T013', 'T013'),
    ('T014', 'T014'),
    ('T015', 'T015'),
]

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
    id_produk = forms.CharField(
        label='ID Produk',
        max_length=10,
        required=True,
        disabled=True,
    )
    id_apotek = forms.CharField(
        label='ID Apotek',
        max_length=10,
        required=True,
        disabled=True,
    )
    id_transaksi_pembelian = forms.CharField(
        label='ID Transaksi Pembelian',
        widget=forms.Select(choices=ID_T0)
    )   
    jumlah = forms.CharField(
        label='jumlah',
        max_length=50,
        required=True,
    )
