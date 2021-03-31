# Generated by Django 3.1.7 on 2021-03-31 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_team_product'),
        ('designation', '0003_designation_team'),
        ('product', '0003_product_company'),
        ('user', '0007_auto_20210331_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='designation_assigned',
        ),
        migrations.AddField(
            model_name='user',
            name='designation_assigned',
            field=models.ManyToManyField(blank=True, to='designation.Designation'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='product_assigned',
        ),
        migrations.AddField(
            model_name='user',
            name='product_assigned',
            field=models.ManyToManyField(blank=True, to='product.Product'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='team_assigned',
        ),
        migrations.AddField(
            model_name='user',
            name='team_assigned',
            field=models.ManyToManyField(blank=True, to='team.Team'),
        ),
    ]