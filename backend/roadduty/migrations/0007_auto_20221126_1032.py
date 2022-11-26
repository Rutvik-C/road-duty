# Generated by Django 3.1 on 2022-11-26 05:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadduty', '0006_auto_20221126_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='amount',
            field=models.IntegerField(blank=True, default=2000, null=True),
        ),
        migrations.AlterField(
            model_name='challan',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
