from django.db import models

# Create your models here.

class Wix(models.Model):
    data = models.JSONField()
