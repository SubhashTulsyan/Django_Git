from django import forms

class studForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


    def clean_name(self):
        val = self.cleaned_data['name']
        if len(val)<4:
            raise forms.ValidationError('Name: Please enter more than 4 words')
        return val

    def clean_email(self):
        val = self.cleaned_data['email']
        if len(val)<8:
            raise forms.ValidationError('Email: Please enter more than 8 words')
        return val

    