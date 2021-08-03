# Generated by Django 3.2 on 2021-04-23 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0010_remove_predictions_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='away',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away', to='football.team', to_field='app_id'),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='home',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home', to='football.team', to_field='app_id'),
        ),
    ]
