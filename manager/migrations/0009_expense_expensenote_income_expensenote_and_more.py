# Generated by Django 4.2.5 on 2023-10-26 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_alter_expense_amount_alter_expense_expensedate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='ExpenseNote',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='income',
            name='ExpenseNote',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='ExpenseDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 12, 17, 17, 998362, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='income',
            name='IncomeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 12, 17, 17, 998362, tzinfo=datetime.timezone.utc)),
        ),
    ]
