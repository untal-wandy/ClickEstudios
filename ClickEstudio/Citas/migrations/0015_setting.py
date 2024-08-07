# Generated by Django 5.0.6 on 2024-06-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0014_servicerelatedimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Setting', max_length=255)),
                ('icon', models.ImageField(upload_to='setting_images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
