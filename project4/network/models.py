from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phoneNumber = models.CharField(blank=True, max_length=64)
    accountKey = models.CharField(blank=True, max_length=64)
    firstName = models.CharField(blank=True, max_length=64)
    lastName = models.CharField(blank=True, max_length=64)
    email = models.CharField(blank=True, max_length=64)
    nric = models.CharField(blank=True, max_length=64)
    pass