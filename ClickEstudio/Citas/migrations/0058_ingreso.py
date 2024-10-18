# Generated by Django 5.0 on 2024-10-17 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0057_role_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]