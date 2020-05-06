from django import forms

ID_PR = [
    ('pr001', 'PR001'),
    ('pr002', 'PR002'),
    ('pr003', 'PR003'),
    ('pr004', 'PR004'),
    ('pr005', 'PR005'),
    ('pr006', 'PR006'),
    ('pr007', 'PR007'),
    ('pr008', 'PR008'),
    ('pr009', 'PR009'),
    ('pr010', 'PR010'),
    ('pr011', 'PR011'),
    ('pr012', 'PR012'),
    ('pr013', 'PR013'),
    ('pr014', 'PR014'),
    ('pr015', 'PR015'),
    ('pr016', 'PR016'),
    ('pr017', 'PR017'),
    ('pr018', 'PR018'),
    ('pr019', 'PR019'),
    ('pr020', 'PR020'),
]

ID_AP = [
    ('ap01', 'AP01'),
    ('ap02', 'AP02'),
    ('ap03', 'AP03'),
    ('ap04', 'AP04'),
    ('ap05', 'AP05'),
]

class CreateProdukApotekForm(forms.Form):
    id_produk = forms.CharField(
        label='ID Produk',
        widget=forms.Select(choices=ID_PR)
    )
    id_apotek = forms.CharField(
        label='ID Apotek',
        widget=forms.Select(choices=ID_AP)
    )
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

class UpdateProdukApotekForm(forms.Form):
    id_produk = forms.CharField(
        label='ID Produk',
        widget=forms.Select(choices=ID_PR)
    )
    id_apotek = forms.CharField(
        label='ID Apotek',
        widget=forms.Select(choices=ID_AP)
    )
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
    
