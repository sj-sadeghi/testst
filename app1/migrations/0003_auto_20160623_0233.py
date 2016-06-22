# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20160623_0155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='person',
        ),
        migrations.AddField(
            model_name='mark',
            name='prs',
            field=models.ForeignKey(null=True, to='app1.Person'),
        ),
    ]
