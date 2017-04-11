# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0019_auto_20170410_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneNum', models.IntegerField()),
                ('category', models.IntegerField(choices=[(0, 'Fire'), (1, 'Traffic Accient'), (2, 'Terrorist Attack'), (3, 'Gas leak')])),
                ('region', models.IntegerField(choices=[(0, 'Central Region'), (1, 'North-East Region'), (2, 'North-West Region'), (3, 'South-East Region'), (4, 'South-West Region')])),
            ],
        ),
    ]