from django import forms

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
    jumlah = forms.CharField(
        label='jumlah',
        max_length=50,
        required=True,
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