from django.shortcuts import render, redirect,  get_object_or_404
from .forms import UserExpenseForm, UserIncomeForm, UpdateExpenseForm, UpdateIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense, Income
from django.utils import timezone
from django.core.paginator import Paginator
import datetime


@login_required
def home(request):
    user = request.user

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

    try:
        averageIncome = totalIncome/nIncome
    except:
        averageIncome = 0


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
    
    try:
        averageExpense = totalExpense/nExpense
    except:
        averageExpense = 0


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

    datesQuery = []
    amountQuery = []
    amountDaily = [0]*31
    key = 0
    month = request.POST.get('month', '10')
    graphDates = []
    for i in range(1, 32):
        graphDates.append(i)


    user = request.user
    queryset = Income.objects.filter(User_id = user, DeletedAt = None, IncomeDate__month=month).order_by('IncomeDate')

    for query in queryset:
        datesQuery.append(query.IncomeDate.strftime("%d"))
        amountQuery.append(query.Amount)

    key = len(datesQuery)-2
    while key>=0:
        if datesQuery[key] == datesQuery[key+1]:
            amountQuery[key] = amountQuery[key] + amountQuery[key+1]
            del amountQuery[key+1]
            del datesQuery[key+1]
        key-=1

    key = 1
    k = 0
    while key<32 and k<len(datesQuery):
        if k==len(datesQuery):
            break
        if(key==int(datesQuery[k])):
            amountDaily[int(datesQuery[k])-1] = amountQuery[k]
            k+=1
        key+=1


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
        'labels' : graphDates,
        'money' : amountDaily,
        'form' : form,
        'incomes' : incomes,
        'pages': p,
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

    # Variables, list, integers.
    month = request.POST.get('month', '10')
    fullDate = []
    datesQuery = []
    amountQuery = []
    amountDaily = [0]*31
    key = 0
    graphDates = []
    for i in range(1, 32):
        graphDates.append(i)


    # User, Query, QuerySet
    user = request.user
    queryset = Expense.objects.filter(User_id = user, DeletedAt = None, ExpenseDate__month=month).order_by('ExpenseDate')
    for query in queryset:
        datesQuery.append(query.ExpenseDate.strftime("%d"))
        amountQuery.append(query.Amount)
        fullDate.append(query.ExpenseDate)


    key = len(datesQuery)-2
    while key>=0:
        if datesQuery[key] == datesQuery[key+1]:
            amountQuery[key] = amountQuery[key] + amountQuery[key+1]
            del amountQuery[key+1]
            del datesQuery[key+1]
        key-=1


    key = 1
    k = 0
    while key<32 and k<len(datesQuery):
        if(key==int(datesQuery[k])):
            amountDaily[int(datesQuery[k])-1] = amountQuery[k]
            k+=1
        key+=1


    # History Pagination.
    p = Paginator(Expense.objects.filter(User_id = user, DeletedAt = None).order_by('-ExpenseDate'), 5)
    page = request.GET.get('page')
    expenses = p.get_page(page)
    print(p.num_pages)

    # API call
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
        'username' : user,
        'labels': graphDates,
        'money' : amountDaily,
        'form' : form,
        'expenses' : expenses,
        'fullDate' : fullDate,
        'pages': p,
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
















# def about(request):
#     amountQuery = []
#     fullDateQuery = []
#     user = request.user
#     queryset = Expense.objects.filter(User_id = user, DeletedAt = None).order_by('-ExpenseDate')
#     for query in queryset:
#         fullDateQuery.append(datetime.strptime(query.ExpenseDate, "%Y-%m-%d")).time()
#         amountQuery.append(query.Amount)
    
#     key = len(fullDateQuery)-2
#     while key>=0:
#         if fullDateQuery[key] == fullDateQuery[key+1]:
#             amountQuery[key] = amountQuery[key] + amountQuery[key+1]
#             del amountQuery[key+1]
#             del fullDateQuery[key+1]
#         key-=1

#     print(len(fullDateQuery))
#     print(len(amountQuery))


#     context = {
#         'username': user,
#         'fullDate' : fullDateQuery,
#         'amount' : amountQuery,
#     }
#     return render(request, 'manager/about.html', context)