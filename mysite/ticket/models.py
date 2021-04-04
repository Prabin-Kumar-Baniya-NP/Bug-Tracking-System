import os
from django.db import models
from ticket.ticket_number import ticket_number_generator
from product.models import Product
from django.utils import timezone
from django.dispatch import receiver
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Ticket(models.Model):
    TICKET_STATUS = [
        ("SUB", "SUBMITTED"),
        ("REJ", "REJECTED"),
        ("A&U", "APPROVED AND UNASSIGNED"),
        ("A&A", "APPROVED AND ASSIGNED"),
        ("POS", "POSTPONED"),
        ("RES", "RESOLVED"),
        ("CLO", "CLOSED"),
        ("DUP", "DUPLICATE"),
    ]
    SEVERITY_LEVEL = [
        ("LOW", "LOW"),
        ("MIN", "MINOR"),
        ("MAJ", "MAJOR"),
        ("CRI", "CRITICAL"),
    ]
    PRIORITY_LEVEL = [
        ("LOW", "LOW"),
        ("MED", "MEDIUM"),
        ("HIG", "HIGH"),
    ]
    ticket_number = models.CharField(max_length = 25, default = ticket_number_generator, editable = False)
    title = models.CharField("Bug Title", max_length = 150)
    description = models.TextField("Bug Description", max_length=500)
    ticket_status = models.CharField(max_length=3, choices = TICKET_STATUS, default = "SUB", null = True, blank = True)
    severity_level = models.CharField(max_length =3, choices = SEVERITY_LEVEL, null = True, blank = True)
    priority_level = models.CharField(max_length =3, choices = PRIORITY_LEVEL, null = True, blank = True)
    public_view = models.BooleanField(default=False)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, default= None)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    submitted_on = models.DateTimeField(default = timezone.now, editable = False)
    screenshot = models.ImageField(upload_to = "ticket/ticket-screenshots/", blank=True,null=True,default=None)
    assigned_to = models.ManyToManyField(User, blank = True, related_name= "User_assigned")

    def __str__(self):
        return self.title

@receiver(models.signals.post_delete, sender=Ticket)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from Ticket
    when corresponding `Ticket` object is deleted.
    """
    if instance.screenshot:
        if os.path.isfile(instance.screenshot.path):
            os.remove(instance.screenshot.path)

@receiver(models.signals.pre_save, sender=Ticket)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from Ticket
    when corresponding `screenshot` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_screenshot = Ticket.objects.get(pk=instance.pk).screenshot
    except Ticket.DoesNotExist:
        return False

    new_screenshot = instance.screenshot
    if not old_screenshot == new_screenshot:
        if os.path.isfile(old_screenshot.path):
            os.remove(old_screenshot.path)