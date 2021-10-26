from django import forms

class studForm(forms.Form):
    def start_s(val):
        if val[0] !='s':
            raise forms.ValidationError('not starting with s')

    name = forms.CharField(validators=[start_s])
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        #print(clean_data)
        val_name = self.cleaned_data['name']
        if len(val_name)<4:
            raise forms.ValidationError('name: less than 4')

        val_email = self.cleaned_data['email']
        if len(val_email)<8:
            raise forms.ValidationError('Email: less than 4')



    