# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_mgm', '0003_auto_20161114_2201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'permissions': (('can_enter', 'Can Enter'),)},
        ),
    ]
