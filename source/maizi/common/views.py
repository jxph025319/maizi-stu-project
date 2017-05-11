#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

from django.shortcuts import render, HttpResponse
from .models import *
import json


# 首页
def index(request):
    rslt = Course.objects.all()
    nrslt = rslt.order_by('-date_publish').values('name', 'date_publish', 'image')
    hrslt = rslt.order_by('-student_count').values('name', 'student_count', 'image')
    prslt = rslt.order_by('-click_count').values('name', 'click_count', 'image')
    adrslt = Ad.objects.all().values('title', 'image_url')
    newsrslt = RecommendedReading.objects.all()
    AVrslt = newsrslt.filter(reading_type='AV').values("title", 'url')
    NWrslt = newsrslt.filter(reading_type='NW').values("title", 'url')
    DCrslt = newsrslt.filter(reading_type='DC').values("title", 'url')
    lkrslt = Links.objects.all().values('title', 'callback_url')
    return render(request, "common/index.html", locals())


# 关键字
def keywds(request):
    anslist = []
    if request.GET['skey'] == 'null':
        ls = RecommendKeywords.objects.all().values_list('name')
    else:
        ls = RecommendKeywords.objects.filter(name__icontains=request.GET['skey']).values_list('name')
    for n in ls:
        anslist.append(n[0])
    return HttpResponse(json.dumps(anslist))


# 课程搜索
def searchkeys(request):
    if request.GET.dict():
        key = request.GET['skey']
    else:
        return HttpResponse("false")
    ans = {}
    ct = Course.objects.filter(name__icontains=key).values_list('name', )
    cct = CareerCourse.objects.filter(name__icontains=key).values_list('name', 'course_color')
    clist = []
    cclist = []
    if ct:
        for n in ct:
            clist.append(n[0])
    if cct:
        for n in cct:
            cclist.append(n)
    if clist:
        ans['couse'] = list(clist)
    else:
        ans['couse'] = None
    if cclist:
        ans['careercourse'] = list(cclist)
    else:
        ans['careercourse'] = None
    print(ans)
    return HttpResponse(json.dumps(ans))

