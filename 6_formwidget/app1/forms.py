from django import forms


class studforms(forms.Form):
    #name = forms.CharField()
    #name = forms.CharField(widget=forms.TextInput(attrs={'class': 'somecssclass'}))
    name = forms.CharField(widget=forms.TimeInput())
    age = forms.IntegerField()
    email = forms.EmailField()
    website = forms.URLField()
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    hid = forms.CharField(widget=forms.HiddenInput)
    dte = forms.DateField()
    dtetime = forms.DateTimeField()
