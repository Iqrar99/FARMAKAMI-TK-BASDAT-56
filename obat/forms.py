from django import forms

class ObatForm(forms.Form):
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