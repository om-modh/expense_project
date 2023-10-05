from rest_framework import generics
from django.shortcuts import render, redirect
from .serializers import ExpenseSerializer
from .forms import UserExpenseForm, UserIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense


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
    if request.method == 'POST':
        form = UserExpenseForm(request.POST)
        print("-------------------------------------------------------------------")
        if form.is_valid():
            form.instance.User_id = request.user
            print("yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
            form.save()
            messages.success(request, f'Your expense data is added Successfully!')
            return redirect('manager-expense')
    else:
        form = UserExpenseForm()
    context = {
        'form' : form
    }
    return render(request, 'manager/expense.html', context)