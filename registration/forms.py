from django import forms

class AdminForm(forms.Form):
    email = forms.EmailField(
        label='Email'
    )
    password = forms.CharField(
        label='Password',
        max_length=64,
        required=True,
        widget=forms.PasswordInput()
    )
    nama_lengkap = forms.CharField(
        label='Nama Lengkap',
        max_length=100,
        required=True
    )
    no_telp = forms.CharField(
        label='No. Telp',
        max_length=15,
        required=True
    )

class ConsumerForm(forms.Form):
    consumer_email = forms.EmailField(label='Email', required=True)
    consumer_password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput(),
        required=True
    )
    consumer_full_name = forms.CharField(label='Nama Lengkap', max_length=100, required=True)
    consumer_telp = forms.CharField(label='No. telp', max_length=15, required=True)

    sex_choices = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan')
    )
    consumer_sex = forms.ChoiceField(
        label='Jenis Kelamin',
        choices=sex_choices,
    )

    consumer_birth_date = forms.DateTimeField(
        label='Tanggal Lahir',
        widget=forms.SelectDateWidget(years=range(1900,2100)),
        required=True
    )
    consumer_address = forms.CharField(label='Alamat', max_length=500)

class KurirForm(forms.Form):
    kurir_email = forms.EmailField(label='Email', required=True)
    kurir_password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput(),
        required=True
    )
    kurir_full_name = forms.CharField(
        label='Nama Lengkap', max_length=100, required=True)
    kurir_telp = forms.CharField(label='No. telp', max_length=15, required=True)
    kurir_company_name = forms.CharField(label='Nama Perusahaan', max_length=100, required=True)

class CSForm(forms.Form):
    cs_email = forms.EmailField(label='Email', required=True)
    cs_password = forms.CharField(
        label='Password',
        max_length=64,
        widget=forms.PasswordInput(),
        required=True
    )
    cs_full_name = forms.CharField(label='Nama Lengkap', max_length=100, required=True)
    cs_telp = forms.CharField(label='No. telp', max_length=15, required=True)
    cs_ktp = forms.CharField(label='No. KTP', max_length=20, required=True)
    cs_sia = forms.CharField(label='No. SIA', max_length=20, required=True)

