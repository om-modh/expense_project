from django import forms
from django.forms.widgets import NumberInput
from .models import Income, Expense


class UserIncomeForm(forms.Form):
    INCOME_CHOICES= [
    ('salary', 'Salary'),
    ('cash', 'Cash'),
    ('divident', 'Divident'),
    ]
    income_amount = forms.IntegerField(label='Amount', widget=NumberInput(attrs={'placeholder':'Amount'}))
    income_date = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    income_image = forms.ImageField(label='Image', required=False)
    income_category = forms.CharField(label='Category', widget=forms.Select(choices=INCOME_CHOICES))

    class Meta:
        model = Income
        fields = ['income_amount', 'income_date', 'income_image', 'income_category']

class UserExpenseForm(forms.ModelForm):
    EXPENSE_CHOICES= [
    ('1', 'Necessity'),
    ('2', 'Desire'),
    ('3', 'Investment')
    ]
    # id = forms.IntegerField(widget=forms.HiddenInput())
    Amount = forms.IntegerField(label='Amount', widget=NumberInput(attrs={'placeholder':'Amount'}))
    ExpenseDate = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    ExpenseImage = forms.ImageField(label='Image', required=False)
    ExpenseCatId = forms.IntegerField(label='Category', widget=forms.Select(choices=EXPENSE_CHOICES))

    class Meta:
        model = Expense
        fields = ['Amount', 'ExpenseDate', 'ExpenseImage', 'ExpenseCatId']

