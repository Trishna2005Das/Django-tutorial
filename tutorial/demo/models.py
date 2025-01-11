from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/')
    date_added =models.DateTimeField(default=timezone.now)
    choice=[('ml','machine learning'),('dl','deep learning')]
    field=models.CharField(max_length=30,choices=choice)
    