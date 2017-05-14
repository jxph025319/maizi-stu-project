# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20170510_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image_url',
            field=models.ImageField(verbose_name='图片路径', upload_to='static/ad/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='links',
            name='image_url',
            field=models.ImageField(verbose_name='图片路径', blank=True, upload_to='static/links/%Y/%m', null=True),
        ),
    ]
