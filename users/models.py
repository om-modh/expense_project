from django.db import models
from django.contrib.auth.models import User
from users.forms import UserRegistrationForm 

class Users(models.Model):
    User_id = models.BigAutoField(primary_key=True)
    Username = models.CharField(max_length=25 ,unique=True, blank=False)
    EmailId = models.CharField(max_length=120 ,unique=True, blank=False)
    BirthDate = models.DateField(blank=False)
    Password = models.CharField(max_length=50)
    PhoneNo = models.CharField(max_length=12, unique=True, blank=False)
    
    def __str__(self):
        return self.Username