# Generated by Django 4.2.5 on 2023-10-27 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_rename_expensenote_income_incomenote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='ExpenseDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 10, 22, 7, 489339, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='income',
            name='IncomeDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 27, 10, 22, 7, 489339, tzinfo=datetime.timezone.utc)),
        ),
    ]