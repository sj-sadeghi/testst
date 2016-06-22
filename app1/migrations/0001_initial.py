# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('grade', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Grade',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('meli_code', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Person',
            },
        ),
        migrations.AddField(
            model_name='mark',
            name='person',
            field=models.ForeignKey(to='app1.Person'),
        ),
    ]
