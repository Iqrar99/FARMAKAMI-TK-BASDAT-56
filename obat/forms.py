from django import forms
from django.db import connection

class Get(object):

    def __init__(self):
        super().__init__()

    def get_id_merk(self):
        """
        function untuk mendapatkan id merk obat yang tersedia pada tabel MERK OBAT.
        """
        cursor = connection.cursor()
        cursor.execute("SET SEARCH_PATH TO farmakami;")
        cursor.execute("SELECT id_merk_obat FROM merk_obat;")

        columns = [col[0] for col in cursor.description]
        data_id = [dict(zip(columns, row)) for row in cursor.fetchall()]

        packed_data = []
        for data in data_id:
            number = int(data['id_merk_obat'][-2:])
            packed_data.append((data['id_merk_obat'], data['id_merk_obat']))

        return tuple(packed_data)

class CreateObatForm(forms.Form):
    g = Get()

    id_merk_obat = forms.ChoiceField(
        label='ID Merk Obat',
        choices=g.get_id_merk()
    )
    netto_obat = forms.CharField(
        label='Netto',
        max_length=10,
    )
    dosis_obat = forms.CharField( 
        label='Dosis',
        max_length=100,
    )
    aturan_pakai = forms.CharField(
        label='Aturan Pakai',
        max_length=100,
        required=False
    )
    kontraindikasi = forms.CharField(
        label='Kontraindikasi',
        max_length=100,
        required=False
    )
    bentuk_kesediaan = forms.CharField(
        label='Bentuk Kesediaan',
        max_length=100,
    )

class UpdateObatForm(forms.Form):
    g = Get()

    id_obat = forms.CharField(
        label='ID Obat',
        disabled=True,
    )
    id_produk = forms.CharField(label='ID Produk', disabled=True)
    id_merk_obat = forms.ChoiceField(
        label='ID Merk Obat' ,
        choices=g.get_id_merk()
    )
    netto_obat = forms.CharField(
        label='Netto',
        max_length=10,
    )
    dosis_obat = forms.CharField(
        label='Dosis',
        max_length=100,
    )
    aturan_pakai = forms.CharField(
        label='Aturan Pakai',
        max_length=100,
        required=False
    )
    kontraindikasi = forms.CharField(
        label='Kontraindikasi',
        max_length=100,
        required=False
    )
    bentuk_kesediaan = forms.CharField(
        label='Bentuk Kesediaan',
        max_length=100,
    )
