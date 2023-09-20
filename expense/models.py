from django.db import models
from users.models import Users
from datetime import datetime

now = datetime.now()

class BudgetTypeMaster(models.Model):
    BudgetMaster = models.BigAutoField(primary_key=True)
    BudgetType = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return f'{self.BudgetType} of {self.User.username}' 
    
class Budget(models.Model):
    Budget_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    BudgetMaster = models.ForeignKey(BudgetTypeMaster, on_delete=models.CASCADE)
    BudgetAmount = models.DecimalField(max_digits=10, decimal_places=2)
    CreatedAt = models.DateTimeField(blank=False, default=now)
    UpdatedAt = models.DateTimeField(blank=False, default=now)
    DeletedAt = models.DateTimeField(blank=False, default=now)
    def __str__(self):
        return f'{self.Budget_id} of {self.Users.Username}'

class IncomeCategories(models.Model):
    IncomeCatId = models.BigAutoField(primary_key=True)
    IncomeType = models.CharField(max_length=25, blank=False)
    CreatedAt = models.DateTimeField(blank=False, default=now)
    UpdatedAt = models.DateTimeField(blank=False, default=now)
    DeletedAt = models.DateTimeField(blank=False, default=now)
    def __str__(self):
        return f'{self.IncomeType} of {self.Users.Username}'

class Income(models.Model):
    income_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    Amount = models.IntegerField(unique=True, blank=False)
    IncomeDate = models.DateTimeField(blank=False)
    IncomeImage = models.ImageField(upload_to='income_pics', blank=True)
    IncomeCatId = models.ForeignKey(IncomeCategories, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(blank=False, default=now)
    UpdatedAt = models.DateTimeField(blank=False, default=now)
    DeletedAt = models.DateTimeField(blank=False, default=now)
    def __str__(self):
        return f'{self.income_id} of {self.Users.Username}'

class ExpenseCategories(models.Model):
    ExpenseCatId = models.BigAutoField(primary_key=True)
    ExpenseType = models.CharField(max_length=25, blank=False)
    CreatedAt = models.DateTimeField(blank=False, default=now)
    UpdatedAt = models.DateTimeField(blank=False, default=now)
    DeletedAt = models.DateTimeField(blank=False, default=now)
    def __str__(self):
        return f'{self.ExpenseType} of {self.Users.Username}'

class Expense(models.Model):
    Expense_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    Amount = models.IntegerField(unique=True, null=False)
    ExpenseDate = models.DateTimeField(null=False)
    ExpenseImage = models.ImageField(upload_to='expense_pics', blank=True)
    ExpenseCatId = models.ForeignKey(ExpenseCategories, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(null=False, default=now)
    UpdatedAt = models.DateTimeField(null=False, default=now)
    DeletedAt = models.DateTimeField(null=False, default=now)
    def __str__(self):
        return f'{self.Expense_id} of {self.Users.Username}'