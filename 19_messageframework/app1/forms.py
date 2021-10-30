from django import forms
from .models import User
class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput
        }