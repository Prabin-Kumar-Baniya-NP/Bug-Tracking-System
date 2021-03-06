import os
from django.db import models
from django.conf import settings
from django.dispatch import receiver
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

@receiver(models.signals.post_delete, sender=Company)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from Company
    when corresponding `Company` object is deleted.
    """
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)

@receiver(models.signals.pre_save, sender=Company)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from Company
    when corresponding `Logo` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_logo = Company.objects.get(pk=instance.pk).logo
    except Company.DoesNotExist:
        return False

    new_logo = instance.logo
    if not old_logo == new_logo:
        if os.path.isfile(old_logo.path):
            os.remove(old_logo.path)