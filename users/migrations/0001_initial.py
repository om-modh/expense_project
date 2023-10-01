# Generated by Django 4.2.5 on 2023-09-30 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=25)),
                ('LastName', models.CharField(max_length=25)),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Email', models.EmailField(max_length=120, unique=True)),
                ('BirthDate', models.DateField()),
                ('PhoneNumber', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('Users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
