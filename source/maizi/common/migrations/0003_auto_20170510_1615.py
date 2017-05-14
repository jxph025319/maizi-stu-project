# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20170504_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careercourse',
            name='image',
            field=models.ImageField(upload_to='static/course/%Y/%m', verbose_name='课程小图标'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='static/course/%Y/%m', verbose_name='课程封面'),
        ),
    ]
