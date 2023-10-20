from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=25, blank=True)
    LastName = models.CharField(max_length=20, blank=True)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    PhoneNumber = PhoneNumberField(unique=True)

    def __str__(self):
        return f'{self.User_id.username} Profile'