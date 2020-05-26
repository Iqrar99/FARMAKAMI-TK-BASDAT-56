from django import forms
from django.db import connection

class CreateObatForm(forms.Form):
    def get_id_merk():
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

    id_merk_obat = forms.ChoiceField(
        label='ID Merk Obat',
        choices=get_id_merk()
    )
    netto_obat = forms.CharField(
        label='Netto',
        max_length=10,
        required=True
    )
    dosis_obat = forms.CharField(
        label='Dosis',
        max_length=100,
        required=True
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
        required=True
    )

class UpdateObatForm(forms.Form):
    id_obat = forms.CharField(label='ID Obat', disabled=True)
    id_produk = forms.CharField(label='ID Produk', disabled=True)
    id_merk_obat = forms.ChoiceField(
        label='ID Merk Obat' ,
        choices=(
            (1, 1),
            (2, 2)
        )
    )
    netto_obat = forms.CharField(
        label='Netto',
        max_length=10,
        required=True
    )
    dosis_obat = forms.CharField(
        label='Dosis',
        max_length=100,
        required=True
    )
    aturan_pakai = forms.CharField(
        label='Aturan Pakai',
        max_length=100,
    )
    kontraindikasi = forms.CharField(
        label='Kontraindikasi',
        max_length=100,
    )
    bentuk_kesediaan = forms.CharField(
        label='Bentuk Kesediaan',
        max_length=100,
        required=True
    )

