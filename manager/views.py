from rest_framework import generics
from django.shortcuts import render, redirect
from .serializers import ExpenseSerializer
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
class expense(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    def expense(request):
        if request.method == 'POST':
            form = UserExpenseForm(request.POST)
            form.fields['id'].initial = request.user.id
            print(request.user.id)
            print("-------------------------------------------------------------------")
            if form.is_valid():
                print("yesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
                form.save()
                messages.success(request, f'Your expense data is added Successfully!')
                return redirect('manager-expense')
        else:
            form = UserExpenseForm()
        return render(request, 'manager/expense.html', {'form' : form})