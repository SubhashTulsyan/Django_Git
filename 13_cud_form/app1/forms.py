from django import forms


class signUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(error_messages={'required':'Enter email'}, min_length=10)