# Generated by Django 5.0.6 on 2024-06-10 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0006_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_choice',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_time_choice',
            field=models.TimeField(default='10:00'),
        ),
    ]
