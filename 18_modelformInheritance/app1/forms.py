from django import forms
from .models import Registration
class StudentForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput
        }

class TeacherForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = ['teacher_name', 'email', 'password']
