from django.db import models
from users.models import User
 
class BudgetTypeMaster(models.Model):
    BudgetMaster = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    BudgetType = models.CharField(max_length=20, blank=False)
    def __str__(self):
        return f'{self.BudgetType} of {self.User_id.username}' 
    
class Budget(models.Model):
    Budget_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    BudgetMaster = models.ForeignKey(BudgetTypeMaster, on_delete=models.CASCADE)
    BudgetAmount = models.DecimalField(max_digits=10, decimal_places=2)
    CreatedAt = models.DateTimeField(auto_now=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    DeletedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.Budget_id} of {self.User_id.username}'

class IncomeCategories(models.Model):
    IncomeCatId = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    IncomeType = models.CharField(max_length=25, blank=False)
    CreatedAt = models.DateTimeField(auto_now=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    DeletedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.IncomeType} of {self.User_id.username}'

class Income(models.Model):
    income_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(unique=True, blank=False)
    IncomeDate = models.DateTimeField(blank=False)
    IncomeImage = models.ImageField(upload_to='income_pics/', blank=True)
    IncomeCatId = models.ForeignKey(IncomeCategories, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField(auto_now=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    DeletedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.income_id} of {self.User_id.username}'

# class ExpenseCategories(models.Model):
#     ExpenseCatId = models.BigAutoField(primary_key=True)
#     User_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     ExpenseType = models.CharField(max_length=25, blank=False)
#     CreatedAt = models.DateTimeField(auto_now=True)
#     UpdatedAt = models.DateTimeField(auto_now=True)
#     DeletedAt = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return f'{self.ExpenseType} of {self.User_id.username}'
    

class Expense(models.Model):
    Expense_id = models.BigAutoField(primary_key=True)
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(unique=True, null=False)
    ExpenseDate = models.DateTimeField(null=False)
    ExpenseImage = models.ImageField(upload_to='expense_pics/', blank=True)
    ExpenseCatId = models.IntegerField(null = False, unique = False)
    CreatedAt = models.DateTimeField(auto_now=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    DeletedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.Expense_id} of {self.User_id.username}'