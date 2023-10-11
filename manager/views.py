from rest_framework import generics
from django.shortcuts import render, redirect
from .serializers import ExpenseSerializer
from .forms import UserExpenseForm, UserIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense, Income

@login_required
def home(request):
    expenses = Income.objects.all()
    data = {
        # "labels": [expense.IncomeDate.strftime('%d') for expense in expenses],
        "labels": ['a', 'b', 'c'],
     
        "values": [int(expense.Amount) for expense in expenses],
    }
    # data = {
    #     "labels": json.dumps(["Label1", "Label2", "Label3"]),
    #     "values": json.dumps([10, 20, 30])
    # }
    return render(request, "manager/home.html", {'data':data})


def about(request):
    return render(request, 'manager/about.html', {'title' : 'about'})

@login_required
def income(request):
    if request.method == 'POST':            
        form = UserIncomeForm(request.POST)
        if form.is_valid():
            form.instance.User_id = request.user
            form.save()
            messages.success(request, f'Your income data is added Successfully!')
            return redirect('manager-income')
    else:
        form = UserIncomeForm()
    context = {
        'form' : form
    }
    return render(request, 'manager/income.html', context)

@login_required
def expense(request):
    if request.method == 'POST':
        form = UserExpenseForm(request.POST)
        if form.is_valid():
            form.instance.User_id = request.user
            form.save()
            messages.success(request, f'Your expense data is added Successfully!')
            return redirect('manager-expense')
    else:
        form = UserExpenseForm()
    context = {
        'form' : form
    }
    return render(request, 'manager/expense.html', context)