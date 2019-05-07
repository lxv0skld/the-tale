# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-04-13 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('object_id', models.BigIntegerField()),
                ('property_type', models.BigIntegerField()),
                ('value', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'properties',
            },
        ),
        migrations.AlterUniqueTogether(
            name='property',
            unique_together=set([('object_id', 'property_type')]),
        ),
    ]