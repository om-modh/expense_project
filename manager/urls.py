from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='manager-home'),
    path('income/', views.income, name='manager-income'),
    path('expense/', views.expense, name='manager-expense'),
    path('deleteExpense/<int:id>', views.DeleteExpense, name="deleteExpense"),
    path('deleteIncome/<int:id>', views.DeleteIncome, name='deleteIncome'),
    path('updateExpense/<int:id>', views.UpdateExpense, name='updateExpense'),
    path('updateIncome/<int:id>', views.UpdateIncome, name='updateIncome'),
    # path('about/', views.about, name='about'),
]