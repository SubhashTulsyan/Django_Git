from django import forms
from django.forms.widgets import HiddenInput

class studentform(forms.Form):
    branches = (
        ('-1', '--Select--'),
        ('CS', 'Computer Science'),
        ('ME', 'Mechanical Engineering'),
    )
    
    name = forms.CharField(max_length=80, initial='Sohan', help_text='Please Enter')
    roll = forms.IntegerField()
    #branch = forms.ChoiceField(choices=branches)
    branch = forms.CharField()
    email = forms.EmailField(
        required=True,
        label='EMAIL',
        label_suffix=' ',
        initial='subh@gmail.com',
        disabled=False,
        help_text='Please Enter Email',
        error_messages={'required': 'Please Enter Mandatory Fields'},
    )
    key = forms.IntegerField(widget=forms.HiddenInput())
