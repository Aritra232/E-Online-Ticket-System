# Generated by Django 4.1.7 on 2023-04-23 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_alter_seat_seat_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='bus_id',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='seat',
            name='bus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.bus'),
        ),
    ]
