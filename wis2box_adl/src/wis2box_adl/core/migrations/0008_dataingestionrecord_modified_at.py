# Generated by Django 5.0.6 on 2024-07-18 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_dataingestionrecord_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataingestionrecord',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
