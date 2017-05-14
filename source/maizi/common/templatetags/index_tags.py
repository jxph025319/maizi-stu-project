#!/usr/bin/env python
# 上面的python可以使用env环境变量下的python路径
"""
Created on 5/11/2017
@author: jxph025319
maizi_website项目中的index_tags模块自定义模板的过滤器。
使用IDE工具：PyCharm
"""

from django import template

register = template.Library()


@register.filter()
def half(value):
    return value//2

