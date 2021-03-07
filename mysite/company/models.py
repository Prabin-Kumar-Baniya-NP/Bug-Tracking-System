from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length = 50)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)    