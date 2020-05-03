from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(
        label = 'Email',
        max_length = 255,
        required = True
    )
    password = forms.CharField(
        label = 'Password',
        max_length = 64,
        required = True,
        widget = forms.PasswordInput()
    )
