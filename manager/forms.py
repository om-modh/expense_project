from django import forms
from django.forms.widgets import NumberInput
from .models import Income, Expense


class UserIncomeForm(forms.ModelForm):
    INCOME_CHOICES= [
    ('1', 'Salary'),
    ('2', 'Cash'),
    ('3', 'Divident'),
    ]
    Amount = forms.IntegerField(label='Amount', widget=NumberInput(attrs={'placeholder':'Amount'}))
    IncomeDate = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    IncomeImage = forms.ImageField(label='Image', required=False)
    IncomeCatId = forms.IntegerField(label='Category', widget=forms.Select(choices=INCOME_CHOICES))
    IncomeNote = forms.CharField(label='Note', required=False, widget=forms.TextInput(attrs={'placeholder': 'Type a Note.'}))

    class Meta:
        model = Income
        fields = ['Amount', 'IncomeDate', 'IncomeImage', 'IncomeCatId', 'IncomeNote']

class UserExpenseForm(forms.ModelForm):
    EXPENSE_CHOICES= [
    ('1', 'Necessity'),
    ('2', 'Desire'),
    ('3', 'Investment')
    ]
    Amount = forms.IntegerField(label='Amount', widget=NumberInput(attrs={'placeholder':'Amount'}))
    ExpenseDate = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    ExpenseImage = forms.ImageField(label='Image', required=False)
    ExpenseCatId = forms.IntegerField(label='Category', widget=forms.Select(choices=EXPENSE_CHOICES))
    ExpenseNote = forms.CharField(label='Note', required=False, widget=forms.TextInput(attrs={'placeholder': 'Type a Note.'}))

    class Meta:
        model = Expense
        fields = ['Amount', 'ExpenseDate', 'ExpenseImage', 'ExpenseCatId', 'ExpenseNote']

class UpdateExpenseForm(forms.ModelForm):
    EXPENSE_CHOICES= [
    ('1', 'Necessity'),
    ('2', 'Desire'),
    ('3', 'Investment')
    ]
    Amount = forms.IntegerField(label='Amount', widget=NumberInput(attrs={'placeholder':'Amount'}))
    ExpenseDate = forms.DateTimeField(label='Date and Time', widget=NumberInput(attrs={'type':'datetime-local'}))
    ExpenseImage = forms.ImageField(label='Image', required=False)
    ExpenseCatId = forms.IntegerField(label='Category', widget=forms.Select(choices=EXPENSE_CHOICES))
    ExpenseNote = forms.CharField(label='Note', required=False, widget=forms.TextInput(attrs={'placeholder': 'Type a Note.'}))

    class Meta:
        model = Expense
        fields = ['Amount', 'ExpenseDate', 'ExpenseImage', 'ExpenseCatId', 'ExpenseNote']