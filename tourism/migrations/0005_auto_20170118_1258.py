# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0004_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='places-image'),
        ),
    ]
