# Generated by Django 5.0 on 2024-12-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0083_customer_date_only_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.CharField(blank=True, default='809-000-0000', max_length=20, null=True),
        ),
    ]