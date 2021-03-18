# Generated by Django 3.1.7 on 2021-03-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('team', '0001_initial'),
        ('designation', '0001_initial'),
        ('user', '0004_auto_20210304_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='designation',
            field=models.ManyToManyField(blank=True, to='designation.Designation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='product',
            field=models.ManyToManyField(blank=True, to='product.Product'),
        ),
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.ManyToManyField(blank=True, to='team.Team'),
        ),
    ]