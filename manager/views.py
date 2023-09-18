from django.shortcuts import render
from .forms import UserExpenseForm, UserIncomeForm

def home(request):
    return render(request, 'manager/home.html')

def about(request):
    return render(request, 'manager/about.html', {'title' : 'about'})

def income(request):
    form = UserIncomeForm
    return render(request, 'manager/income.html', {'form' : form})

def expense(request):
    form = UserExpenseForm()
    return render(request, 'manager/expense.html', {'form' : form})
