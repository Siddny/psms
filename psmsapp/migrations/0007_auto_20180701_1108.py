# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-01 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psmsapp', '0006_auto_20180701_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntools',
            name='availability',
            field=models.CharField(choices=[('book', 'book'), ('assign', 'assign'), ('free', 'free')], max_length=200),
        ),
    ]
