# Generated by Django 5.0.6 on 2024-06-17 01:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0025_alter_customer_reserver_mount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_choice',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
