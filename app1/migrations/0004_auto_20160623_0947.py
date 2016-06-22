# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20160623_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='prs',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='app1.Person'),
            preserve_default=False,
        ),
    ]
