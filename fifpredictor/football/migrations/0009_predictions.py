# Generated by Django 3.2 on 2021-04-23 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0008_standing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.IntegerField(unique=True)),
                ('awayWinPercent', models.FloatField(null=True)),
                ('drawPercent', models.FloatField(null=True)),
                ('homeWinPercent', models.FloatField(null=True)),
                ('predictedResult', models.CharField(max_length=100, null=True)),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away', to='football.team', to_field='app_id')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home', to='football.team', to_field='app_id')),
            ],
        ),
    ]