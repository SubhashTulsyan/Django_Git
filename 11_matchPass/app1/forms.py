from django import forms
from django.forms.widgets import PasswordInput


class signUpForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    pwd = forms.CharField(widget=PasswordInput, label='Password')
    pwd_cfm = forms.CharField(widget=PasswordInput, label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        pwd = self.cleaned_data['pwd']
        pwd_cfm = self.cleaned_data['pwd_cfm']

        if pwd is not pwd_cfm:
            raise forms.ValidationError('Password is not matching')