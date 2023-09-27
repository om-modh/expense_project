from rest_framework import generics
from django.shortcuts import render, redirect
from .serializers import ExpenseSerializer
from .forms import UserExpenseForm, UserIncomeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Expense, Income



@login_required
def home(request):
    return render(request, 'manager/home.html')

def about(request):
    return render(request, 'manager/about.html', {'title' : 'about'})

@login_required
def income(request):
    if request.method == 'POST':
        form = UserIncomeForm(request.POST)
        if form.is_valid():
            user_id = request.user  
            amount = form.cleaned_data['income_amount']
            date = form.cleaned_data['income_date']
            image = form.cleaned_data['income_image']
            cat_id = form.cleaned_data['incomeCatId']
            income = Income(User_id=user_id, Amount=amount, IncomeDate=date, IncomeImage=image, IncomeCatId=cat_id)
            income.save()
            messages.success(request, f'Your income data is added Successfully!')
            return redirect('manager-income')
    else:
        form = UserIncomeForm()
    return render(request, 'manager/income.html', {'form' : form})

@login_required
# class expense(generics.ListCreateAPIView):
#     serializer_class = ExpenseSerializer
def expense(request):
    if request.method == 'POST':
        form = UserExpenseForm(request.POST)
        if form.is_valid():
            user_id = request.user
            amount = form.cleaned_data['expense_amount']
            date = form.cleaned_data['expense_date']
            image = form.cleaned_data['expense_image']
            cat_id = form.cleaned_data['expenseCatId']
            expense = Expense(User_id=user_id, Amount=amount, ExpenseDate=date, ExpenseImage=image, ExpenseCatId=cat_id)
            expense.save()
            messages.success(request, f'Your expense data is added Successfully!')
            return redirect('manager-expense')
    else:
        form = UserExpenseForm()
    return render(request, 'manager/expense.html', {'form' : form})