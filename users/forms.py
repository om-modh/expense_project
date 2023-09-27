from django import forms
# from django.contrib.auth.models import User
from .models import UserDetail
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput


class UserRegistrationForm(forms.Form):
    # GENDER_CHOICES = (
    #     (0, 'Male'),
    #     (1, 'Female'),
    #     (2, 'Not Specified'),
    # )
    # first_name = forms.CharField(label='First Name', max_length=20, empty_value=False)
    # last_name = forms.CharField(label='Last Name', max_length=20)
    # username = forms.CharField(label='Username', max_length=30)
    # Gender = forms.ChoiceField()
    # email = forms.EmailField()
    # DateOfBirth = forms.DateField(label='Birth Date', widget=NumberInput(attrs={'type':'date'}))
    # PhoneNo = forms.CharField(label='Phone Number', max_length=12, min_length=9)
    
    class Meta:
        model = UserDetail
        fields = ['first_name', 'last_name', 'username', 'gender', 'email', 'DateOfBirth', 'PhoneNo', 'password1', 'password2']