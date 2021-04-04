# Generated by Django 3.1.7 on 2021-04-03 11:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0010_ticket_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.ManyToManyField(blank=True, related_name='User_assigned', to=settings.AUTH_USER_MODEL),
        ),
    ]