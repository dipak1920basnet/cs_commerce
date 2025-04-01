from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

#Models for Category

class Category(models.Model):
    category_field = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.category_field}"
    
