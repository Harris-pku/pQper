from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from user.models import User
from commentarea.models import Paper, ShortComment
import requests
import json

from haystack.query import SearchQuerySet


# 搜索引擎功能
# 根据输入的内容
# 会返回可能的 用户的用户名、论文的论文名 用于填入待选框
@csrf_exempt
def SearchForPapersAndUsers(request):
    if request.method == 'GET':
        try :
            response = {
                'code' : 200,
                'msg' : "search success",
                'data' : {
                    'findCommentAreas' : [],
                    'findUserIds' : []
                }
            }
            searchString = request.GET.get('searchString')

            # 查找相关的论文
            # 使用全文索引
            ret = SearchQuerySet().filter(content=searchString)
            for i in ret:
                response['data']['findCommentAreas'].append(i.title)

            # 查找相关的用户
            # 直接全字匹配
            ret = User.objects.filter(user_name=searchString)
            for i in ret:
                response['data']['findUserIds'].append(i.pk)
            return JsonResponse(response)
        except:
            # 多半是数据库挂了
            return JsonResponse({"code" : 300})
    else:
        # 请用 GET
        return JsonResponse({"code" : 600})
        

