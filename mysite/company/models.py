from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length=500, null = True, blank = True)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length = 250, null = True, blank = True)
    date_of_establishment = models.DateField(null = True, blank = True)
    official_email = models.EmailField(null = True, blank = True)
    logo = models.ImageField(upload_to="company/company-logo/",blank=True,null=True,default=None)

    def __str__(self):
        return self.name