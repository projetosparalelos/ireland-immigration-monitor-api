# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_auto_20170118_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
