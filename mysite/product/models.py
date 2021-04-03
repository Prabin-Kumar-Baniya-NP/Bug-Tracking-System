from django.db import models
from django.conf import settings
from company.models import Company


class Product(models.Model):
    name = models.CharField(max_length = 50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True, blank = True)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name