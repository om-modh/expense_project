from django.db import models
from users.models import User

class BudgetTypeMaster(models.Model):
    BudgetMaster = models.IntegerField(primary_key=True)
    BudgetType = models.CharField(max_length=20, null=False)

class Budget(models.Model):
    Budget_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    BudgetMaster = models.ForeignKey(BudgetTypeMaster, on_delete=models.CASCADE)
    BudgetAmount = models.IntegerField(max_length=11)
    CreatedAt = models.DateTimeField(null=False)
    UpdatedAt = models.DateTimeField(null=False)
    DeletedAt = models.DateTimeField(null=False)

class IncomeCategories(models.Model):
    IncomeCatId = models.BigAutoField(primary_key=True)
    IncomeType = models.CharField(max_length=25, null=False)
    CreatedAt = models.DateTimeField(null=False)
    UpdatedAt = models.DateTimeField(null=False)
    DeletedAt = models.DateTimeField(null=False)

class Income(models.Model):
    income_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(max_length=10, unique=True, null=False)
    IncomeDate = models.DateTimeField(null=False)
    IncomeImage = models.ImageField(upload_to='income_pics')
    IncomeCatId = models.ForeignKey(IncomeCategories, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(null=False)
    UpdatedAt = models.DateTimeField(null=False)
    DeletedAt = models.DateTimeField(null=False)

class ExpenseCategories(models.Model):
    ExpenseCatId = models.BigAutoField(primary_key=True)
    ExpenseType = models.CharField(max_length=25, null=False)
    CreatedAt = models.DateTimeField(null=False)
    UpdatedAt = models.DateTimeField(null=False)
    DeletedAt = models.DateTimeField(null=False)

class Expense(models.Model):
    Expense_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(max_length=10, unique=True, null=False)
    ExpenseDate = models.DateTimeField(null=False)
    ExpenseImage = models.ImageField(upload_to='expense_pics')
    ExpenseCatId = models.ForeignKey(ExpenseCategories, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(null=False)
    UpdatedAt = models.DateTimeField(null=False)
    DeletedAt = models.DateTimeField(null=False)
