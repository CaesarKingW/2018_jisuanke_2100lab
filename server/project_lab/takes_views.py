# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .serializer import TakesSerializer


# 最新课程学习记录显示在列表末
@require_http_methods(["POST"])
def show_takes(request):
    response = {}
    try:
        # 获取到前端发送回来的数据：用户的电话号码
        req = json.loads(request.body.decode('utf-8'))
        user = User.objects.get(phone_number=req)
        takes = Takes.objects.filter(user_phone=user).order_by('start_time')
        real_takes = []
        for take in takes:
            real_take = TakesSerializer(take)
            real_takes.append(real_take.data)
        response['list'] = real_takes
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)