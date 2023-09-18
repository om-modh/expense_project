from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    BirthDate = forms.DateField(label='Birth Date', widget=NumberInput(attrs={'type':'date'}))
    PhoneNo = forms.IntegerField(label='Phone Number' ,max_value=10, min_value=10)

    class Meta:
        model = User
        fields = ['username', 'email', 'BirthDate', 'PhoneNo', 'password1', 'password2']
        