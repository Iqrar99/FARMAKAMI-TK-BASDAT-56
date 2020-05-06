from django import forms

ID = [
    ('k01', 'K01'),
    ('k02', 'K02'),
    ('k03', 'K03'),
    ('k04', 'K04'),
    ('k05', 'K05'),
]


class TransaksiPembelianForm(forms.Form):
    id_konsumen = forms.CharField(
        label='ID Konsumen', widget=forms.Select(choices=ID))
