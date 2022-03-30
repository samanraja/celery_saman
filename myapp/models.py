from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female')
)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES, null=True)
    city = models.CharField(max_length=100)
    updated_at = models.DateTimeField(null=True,blank=True)



