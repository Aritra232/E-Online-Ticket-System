# Generated by Django 4.1.7 on 2023-04-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0025_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='nid',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
