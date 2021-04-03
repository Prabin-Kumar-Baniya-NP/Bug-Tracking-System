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

    @property
    def administratorStatus(self):
        user = User.objects.get(id=self.id)
        company_administrator_status = (Company.objects.filter(administrator = user).union(Company.objects.filter(name = user.company_associated, administrator = user))).exists()
        product_administrator_status = True if Product.objects.filter(administrator = user).exists else False
        product_administrator_list = [product.administrator.all() for product in user.product_assigned.all()]
        for administrator in product_administrator_list:
            if user == administrator:
                product_administrator_status = True
        team_administrator_status = True if Team.objects.filter(administrator = user).exists else False
        team_administrator_list = [team.administrator.all() for team in user.team_assigned.all()]
        for administrator in team_administrator_list:
            if user == administrator:
                team_administrator_status = True
        designation_administrator_status = True if Designation.objects.filter(administrator = user).exists else False
        designation_administrator_list = [designation.administrator.all() for designation in user.designation_assigned.all()]
        for administrator in designation_administrator_list:
            if user == administrator:
                designation_administrator_status = True
        adminStatus = {
            'company_administrator': company_administrator_status,
            'product_administrator': product_administrator_status,
            'team_administrator': team_administrator_status,
            'designation_administrator': designation_administrator_status,
        }
        return adminStatus