# Generated by Django 3.2 on 2021-04-23 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0009_predictions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictions',
            name='app_id',
        ),
    ]
