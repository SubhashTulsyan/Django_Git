from django import forms

class StudForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField(max_length=100)
    pwd = forms.CharField(max_length=15, widget=forms.PasswordInput)