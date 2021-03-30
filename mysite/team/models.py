from django.db import models
from django.conf import settings
from product.models import Product

class Team(models.Model):
    name = models.CharField(max_length = 50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name + " - " + self.product.name
