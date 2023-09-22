# Generated by Django 4.2.5 on 2023-09-21 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeCategories',
            fields=[
                ('IncomeCatId', models.BigAutoField(primary_key=True, serialize=False)),
                ('IncomeType', models.CharField(max_length=25)),
                ('CreatedAt', models.DateTimeField(auto_now=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('DeletedAt', models.DateTimeField(auto_now=True)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Amount', models.IntegerField(unique=True)),
                ('IncomeDate', models.DateTimeField()),
                ('IncomeImage', models.ImageField(blank=True, upload_to='income_pics/')),
                ('CreatedAt', models.DateTimeField(auto_now=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('DeletedAt', models.DateTimeField(auto_now=True)),
                ('IncomeCatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.incomecategories')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseCategories',
            fields=[
                ('ExpenseCatId', models.BigAutoField(primary_key=True, serialize=False)),
                ('ExpenseType', models.CharField(max_length=25)),
                ('CreatedAt', models.DateTimeField(auto_now=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('DeletedAt', models.DateTimeField(auto_now=True)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('Expense_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Amount', models.IntegerField(unique=True)),
                ('ExpenseDate', models.DateTimeField()),
                ('ExpenseImage', models.ImageField(blank=True, upload_to='expense_pics/')),
                ('CreatedAt', models.DateTimeField(auto_now=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('DeletedAt', models.DateTimeField(auto_now=True)),
                ('ExpenseCatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.expensecategories')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BudgetTypeMaster',
            fields=[
                ('BudgetMaster', models.BigAutoField(primary_key=True, serialize=False)),
                ('BudgetType', models.CharField(max_length=20)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('Budget_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('BudgetAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('CreatedAt', models.DateTimeField(auto_now=True)),
                ('UpdatedAt', models.DateTimeField(auto_now=True)),
                ('DeletedAt', models.DateTimeField(auto_now=True)),
                ('BudgetMaster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.budgettypemaster')),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
