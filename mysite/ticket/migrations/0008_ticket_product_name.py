# Generated by Django 3.1.7 on 2021-03-31 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_company'),
        ('ticket', '0007_auto_20210331_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='product_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
