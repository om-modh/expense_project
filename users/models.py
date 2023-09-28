from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from phone_field import PhoneField


GENDER_CHOICES = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Not Specified'),
)
class UserProfile(models.Model):
    Users = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=25, blank=False)
    LastName = models.CharField(max_length=25)
    Username = models.CharField(max_length=30, unique=True, null=False)
    Gender = models.IntegerField(choices=GENDER_CHOICES)    
    Email = models.EmailField(max_length=120, unique=True)
    BirthDate = models.DateField()
    PhoneNumber = PhoneField(blank=True)

    def __str__(self):
        return self.Username
