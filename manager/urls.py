from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='manager-home'),
    path('income/', views.income, name='manager-income'),
    path('expense/', views.expense.expense, name='manager-expense'),
]