from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phoneNumber = models.CharField(max_length=64)
    accountKey = models.CharField(max_length=64)
    firstName = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    nric = models.CharField(max_length=64)
    pass
