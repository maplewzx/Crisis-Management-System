# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crisis', '0016_case_place_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='casualties',
            new_name='dead',
        ),
    ]