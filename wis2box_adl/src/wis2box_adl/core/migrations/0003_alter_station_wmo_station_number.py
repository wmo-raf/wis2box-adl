# Generated by Django 5.0.6 on 2024-10-07 06:44

import wis2box_adl.core.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_create_default_data_parameters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='wmo_station_number',
            field=models.CharField(help_text='WMO station number', validators=[wis2box_adl.core.utils.validate_as_integer], verbose_name='WMO Station Number'),
        ),
    ]
