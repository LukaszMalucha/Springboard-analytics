# Generated by Django 2.2 on 2020-11-03 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201023_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatemodel',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 3, 10, 51, 28, 643064)),
        ),
    ]
