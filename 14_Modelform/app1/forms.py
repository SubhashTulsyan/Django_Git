from django import forms
from .models import student
class studentForm(forms.ModelForm):
    #forms field defined has high priority
    #email = forms.EmailField(max_length=10)
    class Meta:
        model = student
        fields = ['name', 'roll', 'email', 'password']
        labels = {
            'name': 'NAME', 'roll': 'ROLL', 'email': 'EMAIL_',
            'password': 'PASSWORD',
        }
        help_text = {
            'name': 'Please help Name',
        }
        error_messages = {
            'name': {
                'required': 'Name is required',
            },
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), 
            'name': forms.TextInput(attrs={'class': 'myclass',
            'placeholder':'Enter Name Place'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'})
        } 