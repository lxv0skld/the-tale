# Generated by Django 3.1.13 on 2021-11-09 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_timers', '0002_auto_20211018_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]