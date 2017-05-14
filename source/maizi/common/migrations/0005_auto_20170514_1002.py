# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20170511_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_middle_thumbnall',
            field=models.ImageField(verbose_name='头像104x104', null=True, max_length=200, upload_to='static/avatar/%Y/%m', blank=True, default='static/avatar/default_middle.png'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_small_thumbnall',
            field=models.ImageField(verbose_name='头像70x70', null=True, max_length=200, upload_to='static/avatar/%Y/%m', blank=True, default='static/avatar/default_small.png'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_url',
            field=models.ImageField(verbose_name='头像220x220', null=True, max_length=200, upload_to='static/avatar/%Y/%m', blank=True, default='static/avatar/default_big.png'),
        ),
    ]
