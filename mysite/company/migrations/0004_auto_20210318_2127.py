# Generated by Django 3.1.7 on 2021-03-18 15:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0003_auto_20210318_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='administrator',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
