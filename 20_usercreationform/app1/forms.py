from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput, label='Password Again')
    # class Meta(UserCreationForm.Meta):
    #     #model = User
    #     fields = ('username', 'first_name', 'last_name', 'email')
    #     labels = {'email': 'Email'}
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {'email': 'Email'}

class ProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined',
        'last_login']

class ProfileAdminForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'