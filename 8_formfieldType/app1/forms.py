from django import forms
from django.forms.widgets import CheckboxInput, NumberInput, TextInput
from django.core.validators import MaxValueValidator, MinValueValidator, validate_slug, validate_unicode_slug
class studForm(forms.Form):

    name = forms.CharField(
        widget=TextInput, #Default
        #empty_value='Empyt',
        min_length=5,
        max_length=10,
        error_messages={
            'required': 'Enter Name',
            'min_length': 'Please enter minimum 5 char',
            'max_length': 'Please enter minimum 10 char',
        },
        strip=True, #Default
    )
    age = forms.IntegerField(
        # widget=NumberInput, #Default
        min_value=2,
        max_value=5,
        # error_messages={
        #     'required': 'Mandatory',
        #     'invalid': 'Invalid Input',
        #     'max_value': 'Exceed max value',
        #     'min_value': 'min value',
        # },
        # validators=[
        #     MaxValueValidator(5),
        #     MinValueValidator(1),
        # ],
    )
    isHandicapped = forms.BooleanField(
        widget=CheckboxInput, #Default
        required=True,
        error_messages={'required': 'Check ya uncheck karo'},
    )

    amount = forms.DecimalField(
        #widget=NumberInput, #Default
        # error_messages={
        #     'required': 'req',
        #     'invalid': 'inv',
        #     'max_value': 'max',
        #     'min_value': 'min',
        #     'max_digit': 'md',
        #     'max_decimal_places': 'mdp',
        #     #'max_whole_digits': 'mwd',
        # },
        max_value=100,
        min_value=2,
        max_digits=3,
        decimal_places=2,
    )

    cm = forms.FloatField(
        widget=forms.NumberInput, #default
        min_value=5,
        max_value=10,
        # error_messages={
        #     'required': 'req',
        #     'invalid': 'inv',
        #     'max_value': 'max',
        #     'min_value': 'min',
        # },
    )

    slg = forms.SlugField(
        widget=TextInput, #Default
        #validate_slug=,
        #validate_unicode_slug=,
        # error_messages={
        #     'required': 'required',
        #     'invalid': 'invalid',
        # },
        allow_unicode=False, #Default

    )
    email = forms.EmailField(
        widget=forms.EmailInput, #Default
        # error_messages={
        #     'required': 'required',
        #     'invalid': 'invalid',
        # },
        min_length=10,
        max_length=100,
    )
    url = forms.URLField(
        widget=forms.URLInput, #Default
        # error_messages={
        #     'required': 'required',
        #     'invalid': 'invalid',
        # },
        min_length=10,
        max_length=100,
    )

    date = forms.DateField(
        widget=forms.DateInput, #Default
        # error_messages={
        #     'required': 'required',
        #     'invalid': 'invalid',
        # },
        input_formats= 'DATE_INPUTS_FORMAT'
    )

    time = forms.TimeField(
        widget=forms.TimeInput, #Default
        # error_messages={
        #     'required': 'required',
        #     'invalid': 'invalid',
        # },
        input_formats= 'TIME_INPUT_FORMATS'
    )

