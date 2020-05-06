from django import forms

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
