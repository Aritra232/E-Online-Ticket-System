# Generated by Django 4.1.7 on 2023-04-25 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0029_air_air_id_planeseat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planeseat',
            name='plane',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service.air'),
        ),
    ]