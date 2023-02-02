from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    token = models.TextField(null=True, blank=True)