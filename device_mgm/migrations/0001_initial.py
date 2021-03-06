# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company_mgm', '0004_auto_20161115_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField(blank=True, default=None, max_length=1024, null=True)),
                ('api_key', models.CharField(max_length=1024)),
                ('api_password', models.CharField(max_length=1024)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device', to='company_mgm.Location')),
            ],
            options={
                'permissions': (('open_door', 'Open door'),),
            },
        ),
    ]
