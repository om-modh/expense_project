from django.db import models
from django.contrib.auth.models import User
from users.forms import UserRegistrationForm 

class User(models.Model):
    User_id = models.BigAutoField(primary_key=True)
    Username = models.CharField(max_length=25 ,unique=True, null=False)
    EmailID = models.CharField(max_length=120 ,unique=True, null=False)
    BirthDate = models.DateField(null=False)
    Password = models.CharField(max_length=50)
    PhoneNo = models.IntegerField(max_length=10, unique=True, null=False)
    