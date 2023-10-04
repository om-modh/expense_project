from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Username'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password1' : forms.PasswordInput(attrs={'placeholder':'Password'}),
            'password2' : forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),
        }
