# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20170513_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='submitter',
            field=models.CharField(default='submitter', max_length=255),
            preserve_default=False,
        ),
    ]
