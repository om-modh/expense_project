from django import forms
from django.forms.widgets import NumberInput
from .models import Income, Expense


class UserIncomeForm(forms.Form):
    INCOME_CHOICES= [
    ('1', 'Salary'),
    ('2', 'Cash'),
    ('3', 'Divident'),
    ]
    income_amount = forms.IntegerField(label='Amount')
    income_date = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    income_image = forms.ImageField(label='Image', required=False)
    income_category = forms.IntegerField(label='Category', widget=forms.Select(choices=INCOME_CHOICES))

    class Meta:
        model = Income
        fields = ['income_amount', 'income_date', 'income_image', 'income_category']

class UserExpenseForm(forms.Form):
    EXPENSE_CHOICES= [
    ('1', 'Necessity'),
    ('2', 'Desire'),
    ('3', 'Investment')
    ]
    expense_amount = forms.IntegerField(label='Amount')
    expense_date = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    expense_image = forms.ImageField(label='Image', required=False)
    expenseCatId = forms.IntegerField(label='Category', widget=forms.Select(choices=EXPENSE_CHOICES))

    class Meta:
        model = Expense
        fields = ['expense_amount', 'expense_date', 'expense_image', 'expenseCatId']

