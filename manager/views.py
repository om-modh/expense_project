from rest_framework import generics
from django.shortcuts import render, redirect
from .serializers import ExpenseSerializer
from .forms import UserExpenseForm, UserIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from django.db.models import Sum

@login_required
def home(request):
    labels = []
    money = []
    user = request.user
    # queryset = Expense.objects.filter(User_id = user).order_by('ExpenseDate')
    temp = Expense.objects.values('ExpenseDate').annotate(total_amount=Sum('Amount')).filter(User_id=user)
    expenseGraph = {item['ExpenseDate']:item['total_amount'] for item in temp}
    # stringDate = expenseGraph.keys().strftime("%d-%m-%Y")
    # labels.append(stringDate)
    # money.append(expenseGraph.values())
    # print(labels)
    # print(money)
    print(expenseGraph)
    context = {
        'labels': labels,
        'money' : money

    }
    return render(request, 'manager/home.html', context)


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