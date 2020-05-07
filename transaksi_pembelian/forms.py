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

    id_konsumen = forms.CharField(
        label='ID Konsumen', widget=forms.Select(choices=ID))
