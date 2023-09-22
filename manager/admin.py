from django.contrib import admin
from .models import BudgetTypeMaster, Budget, ExpenseCategories, Expense, Income, IncomeCategories
 
admin.site.register(BudgetTypeMaster)
admin.site.register(Budget)
admin.site.register(IncomeCategories)
admin.site.register(Income)
admin.site.register(ExpenseCategories)
admin.site.register(Expense)