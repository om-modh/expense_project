from django.db import models
from users.models import User
from django.conf import settings
from django.utils import timezone
 
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


class Income(models.Model):
    Income_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(blank=False, max_length=10)
    IncomeDate = models.DateTimeField(default=timezone.now())
    IncomeImage = models.ImageField(upload_to='static/manager/income_pics/', blank=True, null=True)
    IncomeCatId = models.IntegerField()
    IncomeNote = models.TextField(blank=True)
    CreatedAt = models.DateTimeField(auto_now=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    DeletedAt = models.DateTimeField(null=True, blank=True)  # Allow DeletedAt to be null

    def soft_delete(self):
        self.DeletedAt = timezone.now()
        self.save()

    def __str__(self):
        return f'Income {self.pk} by {self.User_id.username}'

    
class Expense(models.Model):
    # Use the default AutoField for primary key
    Expense_id = models.BigAutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Amount = models.IntegerField(blank=False, max_length=10)  # Use DecimalField for currency amounts
    ExpenseDate = models.DateTimeField(default=timezone.now())
    ExpenseImage = models.ImageField(upload_to='static/manager/expense_pics/', blank=True, null=True)  # Use null=True
    ExpenseCatId = models.IntegerField()  # Use the appropriate field type (ForeignKey or IntegerField)
    ExpenseNote = models.TextField(blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)  # Use auto_now_add for creation timestamp
    UpdatedAt = models.DateTimeField(auto_now=True)
    DeletedAt = models.DateTimeField(null=True, blank=True)  # Allow DeletedAt to be null

    def soft_delete(self):
        self.DeletedAt = timezone.now()
        self.save()
    
    def __str__(self):
        return f'Expense {self.pk} by {self.User_id.username}'


