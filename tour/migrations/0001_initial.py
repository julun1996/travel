# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-05-31 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceKeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=50, verbose_name='景区关键字列表')),
            ],
        ),
        migrations.CreateModel(
            name='TourPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placename', models.CharField(max_length=30, verbose_name='景区名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='票价')),
                ('info', models.TextField(verbose_name='景区简介')),
                ('image', models.ImageField(upload_to='tour/')),
                ('locate', models.CharField(max_length=30, verbose_name='地理位置')),
            ],
        ),
    ]
