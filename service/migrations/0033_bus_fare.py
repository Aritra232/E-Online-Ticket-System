# Generated by Django 4.1.7 on 2023-04-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0032_bus_payment_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='fare',
            field=models.IntegerField(null=True),
        ),
    ]
