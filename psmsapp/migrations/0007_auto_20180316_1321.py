# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psmsapp', '0006_auto_20180316_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameradetail',
            name='status',
            field=models.CharField(choices=[('G', 'Good'), ('F', 'Fair'), ('B', 'Bad')], default=1, max_length=200),
            preserve_default=False,
        ),
    ]
