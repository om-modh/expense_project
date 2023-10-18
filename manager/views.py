from django.shortcuts import render, redirect
from .forms import UserExpenseForm, UserIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from datetime import datetime, timedelta

@login_required
def home(request):
    return render(request, 'manager/home.html')


def about(request):
    return render(request, 'manager/about.html', {'title' : 'about'})

@login_required
def income(request):
    formatted_dates = []
    money = []
    user = request.user
    queryset = Income.objects.filter(User_id = user).order_by('IncomeDate')

    for query in queryset:
        formatted_date = query.IncomeDate.strftime("%d-%m-%Y")
        formatted_dates.append(formatted_date)
        amount = query.Amount
        money.append(float(amount))

    for i in range(len(formatted_dates)-2, 0, -1):
        if formatted_dates[i] == formatted_dates[i+1]:
            money[i] = money[i] + money[i+1]
            del money[i+1]

    unique_formatted_dates = []
    for date in formatted_dates:
        if date not in unique_formatted_dates:
            unique_formatted_dates.append(date)

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
        'labels' : unique_formatted_dates,
        'money' : money,
        'form' : form
    }
    return render(request, 'manager/income.html', context)

@login_required
def expense(request):
    formatted_dates = []
    money = []
    user = request.user
    one_week_ago = datetime.today() - timedelta(days=31)
    #ExpenseDate__gte=one_week_ago,
    queryset = Expense.objects.filter( User_id = user).order_by('ExpenseDate')

    for query in queryset:
        formatted_date = query.ExpenseDate.strftime("%d-%m-%Y")
        formatted_dates.append(formatted_date)
        amount = query.Amount
        money.append(amount)

    for i in range(len(formatted_dates)-2, 0, -1):
        if formatted_dates[i] == formatted_dates[i+1]:
            money[i] = money[i] + money[i+1]
            del money[i+1]

    unique_formatted_dates = []
    for date in formatted_dates:
        if date not in unique_formatted_dates:
            unique_formatted_dates.append(date)

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
        'labels': unique_formatted_dates,
        'money' : money,
        'form' : form
    }
    return render(request, 'manager/expense.html', context)