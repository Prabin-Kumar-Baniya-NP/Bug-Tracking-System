from django.db import models
from django.conf import settings
from product.models import Product
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length=500, default="Team Description")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null = True)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_on = models.DateTimeField(default=timezone.now, editable = False)

    def __str__(self):
        return self.name + " - " + self.product.name
