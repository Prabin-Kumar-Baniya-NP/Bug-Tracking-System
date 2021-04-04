import os
from django.db import models
from django.conf import settings
from company.models import Company
from django.dispatch import receiver

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length=500, default="Product Description")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True, blank = True)
    date_of_launch = models.DateField(null = True, blank = True)
    logo = models.ImageField(upload_to="product/product-logo/",blank=True,null=True,default=None)
    administrator = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.name

@receiver(models.signals.post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes Logo from Product
    when corresponding `Logo` object is deleted.
    """
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)

@receiver(models.signals.pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from Product
    when corresponding `Logo` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_logo = Product.objects.get(pk=instance.pk).logo
    except Product.DoesNotExist:
        return False

    new_logo = instance.logo
    if not old_logo == new_logo:
        if os.path.isfile(old_logo.path):
            os.remove(old_logo.path)