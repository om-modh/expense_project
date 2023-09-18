from django import forms
from django.forms.widgets import NumberInput

class UserIncomeForm(forms.Form):
    INCOME_CHOICES= [
    ('salary', 'Salary'),
    ('cash', 'Cash'),
    ('divident', 'Divident'),
    ]
    income_amount = forms.IntegerField(label='Amount')
    income_date = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    income_image = forms.ImageField(label='Image', required=False)
    income_category = forms.CharField(label='Category', widget=forms.Select(choices=INCOME_CHOICES))

class UserExpenseForm(forms.Form):
    EXPENSE_CHOICES= [
    ('necessity', 'Necessity'),
    ('desire', 'Desire'),
    ('investment', 'Investment')
    ]
    expense_amount = forms.IntegerField(label='Amount')
    expense_date = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    expense_image = forms.ImageField(label='Image', required=False)
    expense_category = forms.CharField(label='Category', widget=forms.Select(choices=EXPENSE_CHOICES))

