# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 04:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('psmsapp', '0002_auto_20180314_0508'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Camera',
            new_name='CameraDetail',
        ),
    ]