# Generated by Django 3.1.7 on 2021-03-07 10:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('designation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='administrator',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
