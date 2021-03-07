from django.db import models
from django.contrib.auth.models import AbstractUser
from company.models import Company
from product.models import Product
from team.models import Team
from designation.models import Designation

class User(AbstractUser):
    about_me = models.TextField("About me", max_length=500, blank=True)
    address = models.CharField("Address", max_length=30, blank=True)
    birth_date = models.DateField("Date of birth", null=True, blank=True)
    company_associated = models.ForeignKey(Company, on_delete=models.CASCADE, null = True, blank = True)
    product_assigned = models.ManyToManyField(Product, blank = True)
    team_assigned = models.ManyToManyField(Team, blank = True)
    designation_assigned = models.ManyToManyField(Designation, blank = True)