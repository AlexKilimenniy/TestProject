# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-14 19:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmessage',
            name='post_user',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Хозяин поста: '),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 14, 22, 22, 7, 187184)),
        ),
        migrations.AlterField(
            model_name='postmessage',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 14, 22, 22, 7, 186181)),
        ),
    ]
