# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_mgm', '0002_auto_20161113_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
    ]
