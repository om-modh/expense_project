# Generated by Django 4.2.5 on 2023-09-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_expense_expensecatid_delete_expensecategories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='User_id',
            new_name='id',
        ),
    ]