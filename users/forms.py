from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'placeholder':'Email Address'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']  
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
        }

class PlaceholderAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))

# class UserProfileUpdate(UserCreationForm):
#     first_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    
#     class Meta:
#         model = Profile