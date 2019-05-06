# -*- coding: utf-8 -*-
"""
如果url为空则执行index_view.py
index返回一个html文件：index.html
"""
# from django.http import HttpResponse
from django.shortcuts import render
# from django.views.decorators import csrf


def index(request):
    context = {}
    return render(request, 'index.html', context)
