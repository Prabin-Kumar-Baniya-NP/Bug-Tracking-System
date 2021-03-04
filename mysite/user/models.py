from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    about_me = models.TextField("About me", max_length=500, blank=True)
    address = models.CharField("Address", max_length=30, blank=True)
    birth_date = models.DateField("Date of birth", null=True, blank=True)