from django import forms

ID_KU = [
    ('ku001', 'KU001'),
    ('ku002', 'KU002'),
    ('ku003', 'KU003'),
    ('ku004', 'KU004'),
    ('ku005', 'KU005'),
]
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

class PengantaranForm(forms.Form):
    waktu = forms.CharField(
        label='waktu',
        max_length=50,
        required=True,
    )
    biaya_kirim = forms.CharField(
        label='Biaya Kirim',
        max_length=30,
        required=True
    )

class UpdatePengantaranForm(forms.Form):
        id_pengantaran = forms.CharField(
        label='ID Pengantaran',
        max_length=10,
        required=True,
        disabled=True,
    )
        id_kurir = forms.CharField(
        label='ID Kurir',
        disabled=True,
        widget=forms.Select(choices=ID_KU)

    )
        id_transaksi = forms.CharField(
        label='ID Transaksi',
        disabled=True,
        widget=forms.Select(choices=ID_T0)
    )
        waktu = forms.CharField(
        label='Waktu',
        max_length=50,
        required=True,
    )
        status = forms.CharField(
        label='Status',
        max_length=50,
        required=True,
    )
        biaya_kirim = forms.CharField(
        label='biaya_kirim',
        max_length=50,
        required=True,
    )
        total_biaya = forms.CharField(
        label='total_biaya',
        max_length=50,
        required=True,
        disabled=True,
    )


