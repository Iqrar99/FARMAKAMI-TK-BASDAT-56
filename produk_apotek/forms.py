from django import forms

class ProdukApotekForm(forms.Form):
    harga_jual = forms.CharField(
        label='Harga Jual',
        max_length=15,
        required=True
    )
    satuan_penjualan = forms.CharField(
        label='Satuan Penjualan',
        max_length=5,
        required=True
    )  
    stok = forms.CharField(
        label='Stok',
        max_length=10,
        required=True
    )
    