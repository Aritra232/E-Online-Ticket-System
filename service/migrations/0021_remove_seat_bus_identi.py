# Generated by Django 4.1.7 on 2023-04-23 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_seat_bus_identi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='bus_identi',
        ),
    ]
