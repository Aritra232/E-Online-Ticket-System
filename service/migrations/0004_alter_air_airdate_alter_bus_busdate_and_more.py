# Generated by Django 4.1.7 on 2023-04-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_air_airdate_bus_busdate_train_tdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air',
            name='airDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='busDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='train',
            name='tDate',
            field=models.DateField(null=True),
        ),
    ]
