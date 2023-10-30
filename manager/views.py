from django.shortcuts import render, redirect
from .forms import UserExpenseForm, UserIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from django.utils import timezone
from django.core.paginator import Paginator
from django.views import View

@login_required
def home(request):
    user = request.user
    return render(request, 'manager/home.html', {'username' : user})



@login_required
def income(request):
    formatted_dates = []
    money = []
    user = request.user
    queryset = Income.objects.filter(User_id = user, DeletedAt = None).order_by('IncomeDate')

    for query in queryset:
        formatted_date = query.IncomeDate.strftime("%d-%m-%Y")
        formatted_dates.append(formatted_date)
        amount = query.Amount
        money.append(amount)

    for i in range(len(formatted_dates)-2, -1, -1):
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

    p = Paginator(Income.objects.filter(DeletedAt = None).order_by('-IncomeDate'), 5)
    page = request.GET.get('page')
    incomes = p.get_page(page)

    context = {
        'username' : user,
        'labels' : unique_formatted_dates,
        'money' : money,
        'form' : form,
        'incomes' : incomes,
    }
    return render(request, 'manager/income.html', context)

def DeleteIncome(request, id):
    delete = Income.objects.get(Income_id = id)
    delete.DeletedAt = timezone.now()
    delete.save()
    return redirect('manager-income')

def UpdateIncome(request, id):
    print(id)
    return redirect('manager-income')





@login_required
def expense(request):
    formatted_dates = []
    money = []
    user = request.user
    queryset = Expense.objects.filter(User_id = user, DeletedAt = None).order_by('ExpenseDate')

    for query in queryset:
        formatted_date = query.ExpenseDate.strftime("%d-%m-%Y")
        formatted_dates.append(formatted_date)
        amount = query.Amount
        money.append(amount)

    for i in range(len(formatted_dates)-2, -1, -1):
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
    
    p = Paginator(Expense.objects.filter(User_id = user, DeletedAt = None).order_by('-ExpenseDate'), 5)
    page = request.GET.get('page')
    expenses = p.get_page(page)

    context = {
        'username' : user,
        'labels': unique_formatted_dates,
        'money' : money,
        'form' : form,
        'expenses' : expenses,
    }
    return render(request, 'manager/expense.html', context)

def DeleteExpense(request, id):
    print(id)
    delete = Expense.objects.get(Expense_id = id)
    delete.DeletedAt = timezone.now()
    delete.save()
    return redirect('manager-expense') 
    
def UpdateExpense(request, id):

    return redirect('manager-expense')

