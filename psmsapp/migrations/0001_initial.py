# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CameraDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20, null=True)),
                ('date_added', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'Camera',
                'verbose_name': 'Camera',
                'verbose_name_plural': 'Cameras',
            },
        ),
        migrations.CreateModel(
            name='CameraTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'CameraTypes',
                'verbose_name': 'CameraType',
                'verbose_name_plural': 'CameraTypes',
            },
        ),
        migrations.AddField(
            model_name='cameradetail',
            name='camera_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='psmsapp.CameraTypes'),
        ),
    ]