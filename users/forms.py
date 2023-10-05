from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirm'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']  
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
        }
