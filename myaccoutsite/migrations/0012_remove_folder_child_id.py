# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 06:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myaccoutsite', '0011_auto_20160512_0600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='child_id',
        ),
    ]