from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    BirthDate = forms.DateField(label='Birth Date', widget=NumberInput(attrs={'type':'date'}))
    PhoneNo = forms.CharField(label='Phone Number', max_length=12, min_length=9)

    class Meta:
        model = User
        fields = ['username', 'email', 'BirthDate', 'PhoneNo', 'password1', 'password2']
        