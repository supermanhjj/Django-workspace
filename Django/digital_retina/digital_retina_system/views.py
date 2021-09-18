from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
# from models import Book
from rest_framework import serializers
import json
from django.views.decorators.http import require_http_methods

import json

# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def testapi(request):
    print(request)
    print(request.method)
    if request.method == "GET":
        print(request.GET.get('aa'))
        resp = {'errorcode': 100, 'type': 'Get', 'data': {'main': request.GET.get('aa')}}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        print(request.POST)
        print(request.body)
        str1 = str(request.body, encoding="utf-8")
        data = eval(str1)
        print(data)
        print(data['aa'])
        print(type(request.body))
        resp = {'errorcode': 100, 'type': 'Post', 'data': {'main': data['aa']}}
        return HttpResponse(json.dumps(resp), content_type="application/json")

class DataTest(APIView):
    def get(self,request,*args,**kwargs):
        print('请求后台数据成功！')
        return Response(['后台列表数据1','后台列表数据2'])

class Search(APIView):
    def get(self,request):
        kw = request.GET.get('0', None)
        print(request.GET.get('0', None))
        if kw != None:
            return Response("您搜索的数据为：" + kw)
        else:
            return Response("没有搜索到任何数据")

