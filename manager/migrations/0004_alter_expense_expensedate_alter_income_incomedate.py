# Generated by Django 4.2.5 on 2023-10-20 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_expense_expensedate_alter_income_incomedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='ExpenseDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 13, 43, 31, 838134, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='income',
            name='IncomeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 13, 43, 31, 838134, tzinfo=datetime.timezone.utc)),
        ),
    ]
