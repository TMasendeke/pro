# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-12-22 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteInfo', '0007_t_urls_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='t_dict',
            new_name='t_dictionary',
        ),
    ]
