# Generated by Django 5.0.6 on 2024-07-03 10:35

import timezone_field.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_network_plugin'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='UTC', help_text='Timezone used by the station for recording observations', verbose_name='Station Timezone'),
        ),
    ]
