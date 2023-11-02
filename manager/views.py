from django.shortcuts import render, redirect,  get_object_or_404
from .forms import UserExpenseForm, UserIncomeForm, UpdateExpenseForm, UpdateIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from django.utils import timezone
from django.core.paginator import Paginator


@login_required
def home(request):
    user = request.user

    labelsExpense = ["Necessity", "Desire", "Investment"]
    sumExpense = [0, 0, 0]
    totalExpense = 0
    expenseQuerySet = Expense.objects.filter(User_id = user, DeletedAt = None)
    nExpense = len(expenseQuerySet)
    for query in expenseQuerySet:
        totalExpense += query.Amount
        if query.ExpenseCatId == 1:
            sumExpense[0] = sumExpense[0] + query.Amount
        elif query.ExpenseCatId == 2:
            sumExpense[1] = sumExpense[1] + query.Amount
        else:
            sumExpense[2] = sumExpense[2] + query.Amount

    averageExpense = totalExpense/nExpense


    labelsIncome = ["Salary", "Cash", "Divident"]
    sumIncome = [0, 0, 0]
    totalIncome = 0
    incomeQuerySet = Income.objects.filter(User_id = user, DeletedAt = None)
    nIncome = len(incomeQuerySet)
    for query in incomeQuerySet:
        totalIncome += query.Amount
        if query.IncomeCatId == 1:
            sumIncome[0] = sumIncome[0] + query.Amount
        elif query.IncomeCatId == 2:
            sumIncome[1] = sumIncome[1] + query.Amount
        else:
            sumIncome[2] = sumIncome[2] + query.Amount

    averageIncome = totalIncome/nIncome


    context = { 
        'username': user,
        'labelsExpense' : labelsExpense,
        'sumExpense' : sumExpense,
        'totalExpense' : totalExpense,
        'averageExpense': round(averageExpense, 2),
        'labelsIncome' : labelsIncome,
        'sumIncome' : sumIncome,
        'totalIncome' : totalIncome,
        'averageIncome' : round(averageIncome, 2), 
    }
    return render(request, 'manager/home.html', context)


#INCOME---------------------------------------------------------------------------------------------------------------------

@login_required
def income(request):
    formatted_dates = []
    money = []
    user = request.user
    queryset = Income.objects.filter(User_id = user, DeletedAt = None).order_by('IncomeDate')

    for query in queryset:
        formatted_dates.append(query.IncomeDate.strftime("%d-%m-%Y"))
        money.append(query.Amount)

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

    p = Paginator(Income.objects.filter(User_id = user, DeletedAt = None).order_by('-IncomeDate'), 5)
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

@login_required
def DeleteIncome(request, id):
    delete = Income.objects.get(Income_id = id)
    delete.DeletedAt = timezone.now()
    delete.save()
    return redirect('manager-income')

@login_required
def UpdateIncome(request, id):
    income = get_object_or_404(Income, pk=id)
    
    if request.method == 'POST':
        form = UpdateIncomeForm(request.POST, request.FILES, instance = income)
        if form.is_valid():
            income.Amount = form.cleaned_data['Amount']
            income.IncomeDate = form.cleaned_data['IncomeDate']
            income.IncomeImage = form.cleaned_data['IncomeImage']
            income.IncomeCatId = form.cleaned_data['IncomeCatId']
            income.IncomeNote = form.cleaned_data['IncomeNote']
            income.UpdatedAt = timezone.now()
            income.save()
            return redirect('manager-income')

    else:
        form = UpdateIncomeForm(instance=income)

    return render(request, 'manager/updateIncome.html', {'form': form})




#EXPENSE---------------------------------------------------------------------------------------------------------------------

@login_required
def expense(request):
    formatted_dates = []
    money = []
    monthsQuery = []
    user = request.user
    queryset = Expense.objects.filter(User_id = user, DeletedAt = None).order_by('ExpenseDate')

    for query in queryset:
        formatted_dates.append(query.ExpenseDate.strftime("%d-%m-%Y"))
        monthsQuery.append(query.ExpenseDate.strftime("%m"))
        money.append(query.Amount)

    for i in range(len(formatted_dates)-2, -1, -1):
        if formatted_dates[i] == formatted_dates[i+1]:
            money[i] = money[i] + money[i+1]
            del money[i+1]

    months = [0]*31
    unique_months = []
    unique_formatted_dates = []
    i = 0
    for date in formatted_dates:
        if date not in unique_formatted_dates:
            unique_formatted_dates.append(date)
            unique_months.append(monthsQuery[i]) 
        i+=1
    for k in range(len(unique_formatted_dates)-1):
        if(unique_months[k] == "10"):
            print(k, int(unique_formatted_dates[k][0:2:1]))
            months[int(unique_formatted_dates[k][0:2:1])-1] = money[k]



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
        'money' : months,
        'form' : form,
        'expenses' : expenses,
    }
    return render(request, 'manager/expense.html', context)

@login_required
def DeleteExpense(request, id):
    delete = Expense.objects.get(Expense_id = id)
    delete.DeletedAt = timezone.now()
    delete.save()
    return redirect('manager-expense') 
    
@login_required
def UpdateExpense(request, id):
    expense = get_object_or_404(Expense, pk=id)
    
    if request.method == 'POST':
        form = UpdateExpenseForm(request.POST, request.FILES, instance = expense)
        if form.is_valid():
            expense.Amount = form.cleaned_data['Amount']
            expense.ExpenseDate = form.cleaned_data['ExpenseDate']
            expense.ExpenseImage = form.cleaned_data['ExpenseImage']
            expense.ExpenseCatId = form.cleaned_data['ExpenseCatId']
            expense.ExpenseNote = form.cleaned_data['ExpenseNote']
            expense.UpdatedAt = timezone.now()
            expense.save()
            return redirect('manager-expense')
        
    else:
        form = UpdateExpenseForm(instance=expense)

    return render(request, 'manager/updateExpense.html', {'form': form})

