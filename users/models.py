from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver
