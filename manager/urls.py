from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='manager-home'),
    path('income/', views.income, name='manager-income'),
    path('expense/', views.expense, name='manager-expense'),
    path('deleteExp/<int:id>', views.DeleteExp, name="deleteExp"),
    path('updateExpense/<int:id>', views.UpdateExpense, name='updateExpense'),
]