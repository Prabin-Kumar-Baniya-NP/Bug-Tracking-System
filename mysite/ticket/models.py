from django.db import models
from ticket.ticket_number import ticket_number_generator
from product.models import Product
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