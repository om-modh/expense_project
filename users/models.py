from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver


# GENDER_CHOICES = (
#     (0, 'Male'),
#     (1, 'Female'),
#     (2, 'Not Specified')
# )
class UserDetail(models.Model):
    Users = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=25, blank=False)
    LastName = models.CharField(max_length=25)
    Username = models.CharField(max_length=30, unique=True, null=False)
    # gender = models.IntegerField(choices=GENDER_CHOICES)    
    Email = models.EmailField(max_length=120, unique=True)
    BirthDate = models.DateField()
    PhoneNumber = PhoneField(blank=True)

    def __str__(self):
        return self.Username



# class User(AbstractUser):
#     User_id = 
#     def __str__(self):
#         return self.Username
    

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.CharField(null=True, max_length=200)
#     birth_date = models.DateField(null=True, blank=True)
#     profile_pic = models.ImageField(default='default.jpg', upload_to='profiles_pics')
#     hobby = models.CharField(null=True, max_length=200)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()