# Generated by Django 3.1.7 on 2021-03-31 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_company'),
        ('team', '0003_team_product'),
        ('designation', '0003_designation_team'),
        ('user', '0006_auto_20210307_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='designation_assigned',
        ),
        migrations.AddField(
            model_name='user',
            name='designation_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='designation.designation'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='product_assigned',
        ),
        migrations.AddField(
            model_name='user',
            name='product_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.RemoveField(
            model_name='user',
            name='team_assigned',
        ),
        migrations.AddField(
            model_name='user',
            name='team_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='team.team'),
        ),
    ]
