from django import forms
from .models import User, UserDetail
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import NumberInput
# from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    # FirstName = forms.CharField(label='First Name', max_length=20, empty_value=False)
    # LastName = forms.CharField(label='Last Name', max_length=20)
    # username = forms.CharField(label='Username', max_length=30)
    # DateOfBirth = forms.DateField(label='Birth Date', widget=NumberInput(attrs={'type':'date'}))
    # PhoneNo = forms.CharField(label='Phone Number', max_length=12, min_length=9)
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'FirstName' : forms.TextInput(attrs={'class': 'top-row field-wrap'}),
        #     'LastName' : forms.TextInput(attrs={'class' : 'top-row field-wrap'}),
        # }
    
    
    
    
    
# class UserRegistrationForm(UserCreationForm):
#     class Meta:
#         model = UserProfile
#         fields = ['FirstName', 'LastName', 'Email', 'Gender', 'BirthDate', 'PhoneNumber', 'password1', 'password2']
#         # widgets = {
#         #     'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
#         # }
    
    
    
    
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
