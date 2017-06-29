# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170628_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='MainImage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='Price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]