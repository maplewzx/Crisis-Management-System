# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0018_case_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (2, 'Female')]),
        ),
        migrations.AlterField(
            model_name='case',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='case',
            name='phoneNum',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='case',
            name='region',
            field=models.IntegerField(),
        ),
    ]
