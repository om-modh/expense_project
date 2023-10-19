from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=25, blank=True)
    LastName = models.CharField(max_length=20, blank=True)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    PhoneNumber = models.PhoneNumberField(_(""))