from django import forms
from django.forms.widgets import PasswordInput


class signUpForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    name = forms.CharField(min_length=2)
    email = forms.EmailField(error_messages={'required':'Enter email'}, min_length=10)
    pwd = forms.CharField(widget=PasswordInput, label='Password')
    pwd_cfm = forms.CharField(widget=PasswordInput, label='Confirm Password')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pwd = self.cleaned_data['pwd']
    #     pwd_cfm = self.cleaned_data['pwd_cfm']

    #     if pwd is not pwd_cfm:
    #         raise forms.ValidationError('Password is not matching')