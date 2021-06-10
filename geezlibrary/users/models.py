from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    username = models.CharField(unique= True, max_length=150)
    REQUIRED_FIELDS = ['username','phone_number']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email