from django.db import models
from django.conf import settings
from team.models import Team

class Designation(models.Model):
    name = models.CharField(max_length = 50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null = True)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)