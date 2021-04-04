# Generated by Django 3.1.7 on 2021-04-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20210330_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='date_of_establishment',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='company/company-logo/'),
        ),
        migrations.AddField(
            model_name='company',
            name='official_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
