from django.shortcuts import render
from .forms import UserExpenseForm, UserIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'manager/home.html')

def about(request):
    return render(request, 'manager/about.html', {'title' : 'about'})

@login_required
def income(request):
    form = UserIncomeForm()
    if form.is_valid():
        messages.success(request, f'Your income data is added Successfully!')
    return render(request, 'manager/income.html', {'form' : form})

@login_required
def expense(request):
    form = UserExpenseForm()
    if form.is_valid():
        messages.success(request, f'Your expense data is added Successfully!')
    return render(request, 'manager/expense.html', {'form' : form})
