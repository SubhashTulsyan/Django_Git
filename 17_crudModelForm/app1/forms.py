from django import forms
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        #fields = ['id', 'name', 'roll', 'password']
        fields = '__all__'
        exclude = ['password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'},
            render_value=True),

        }