# Generated by Django 5.0.6 on 2024-05-19 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0002_appointment_date_remember_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='example@gmail.com', max_length=254),
        ),
    ]
