# Generated by Django 4.1.7 on 2023-04-19 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_userinfo_alter_bususer_businfo_alter_bususer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='total_seats',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('is_booked', models.BooleanField(default=False)),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.bus')),
            ],
        ),
    ]
