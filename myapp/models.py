#from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class customers(models.Model):
    username= models.CharField(max_length=100)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)

  