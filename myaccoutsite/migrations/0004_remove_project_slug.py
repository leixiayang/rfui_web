# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccoutsite', '0003_auto_20160405_0316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
    ]
