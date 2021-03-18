# Generated by Django 3.1.7 on 2021-03-18 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_company'),
        ('team', '0002_team_administrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
