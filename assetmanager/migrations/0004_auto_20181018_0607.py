# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assetmanager', '0003_auto_20181014_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetmanager',
            name='asset_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetname.Assetname'),
        ),
    ]