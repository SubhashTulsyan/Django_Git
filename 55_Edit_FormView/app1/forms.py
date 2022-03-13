from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {"doj": forms.DateInput(attrs={"type": "date"}, format=("%d/%m/%Y"))}
