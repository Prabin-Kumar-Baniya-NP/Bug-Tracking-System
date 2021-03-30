from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length=500, null = True, blank = True)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name