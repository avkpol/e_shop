# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='descr',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='good',
            new_name='product',
        ),
        migrations.AddField(
            model_name='good',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='good',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 16, 56, 38, 421081, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 15, 16, 58, 21, 336954, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
