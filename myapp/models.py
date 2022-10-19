from distutils.command.upload import upload
from email.policy import default
from enum import unique
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

from django.contrib.auth.models import AbstractUser



# Create your models here
class Location(models.Model):    
     firstname = models.CharField(max_length = 45)
     lastname = models.CharField(max_length = 45)

     age = models.CharField(max_length =5, default="")
     phone_number= models.CharField(max_length =10, default="") 

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)     

class CustomUser(AbstractUser):    
    username = models.CharField(max_length=45,  default="")
    email = models.EmailField(max_length=30, unique=True)
    age= models.CharField(max_length=5, default="")
    phone_number=models.CharField(max_length=10)
    photo= models.ImageField(upload_to ='images')
         

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
 
 


