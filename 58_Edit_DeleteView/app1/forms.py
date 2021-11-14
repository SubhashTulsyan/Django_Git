from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'myclass'}),
            'roll': forms.NumberInput(attrs={'class': 'myclass'}),
            'doj': forms.DateInput(attrs={'class': 'myclass'}),
        }
