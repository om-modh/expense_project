from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    Users = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=25, blank=False)
    LastName = models.CharField(max_length=25)
    Username = models.CharField(max_length=30, unique=True, null=False)
    Email = models.EmailField(max_length=120, unique=True)
    DateOfBirth = models.DateField()

    def __str__(self):
        return self.Username
