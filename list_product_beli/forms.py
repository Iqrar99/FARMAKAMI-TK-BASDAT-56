from django import forms

class ListProdukForm(forms.Form):
    jumlah = forms.CharField(
        label='jumlah',
        max_length=50,
        required=True,
    )

