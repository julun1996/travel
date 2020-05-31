# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-05-31 08:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tour', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tourplace',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='placekeyword',
            name='titleid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.TourPlace'),
        ),
    ]
