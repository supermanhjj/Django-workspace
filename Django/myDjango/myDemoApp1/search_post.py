# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf

# 接收POST请求数据
def search_post(request):
    ctx ={}
    # if request.POST:
    if request.method == "POST":
        ctx['rlt'] = request.POST['search']
    return render(request, "search_post.html", ctx)
