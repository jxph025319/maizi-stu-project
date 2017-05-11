#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
users模块的url配置。
"""

from django.conf.urls import patterns
from django.conf.urls import include, url
from users.views import userin

urlpatterns = patterns('users.views',
    url(r'^login/?$', userin, name='login'),
)
