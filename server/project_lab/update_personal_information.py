# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
import datetime
import os
# from PIL import Image
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

a = ''


@require_http_methods(['POST', 'GET'])
def update_avator(request):
    response = {}
    try:
        if request.method == 'POST':
            # 获取对象
            b = request.FILES.get('file')
            # if b:
            #     img=Image.open(b)
            #     img.save(BASE_DIR+"/project_lab/static/media/user_photos/"+b.name)
            # b.name = "user_photos/"+ b.name  
            # user_phone = request.Post.get('user_phone')
            new = User.objects.get(phone_number=a)
            new.head_protrait=b
            new.save()
            # old_user=User.objects.get(phone_number=a)
            # response['msg'] = b.name()
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def get_user_phone(request):
    response = {}
    try:
        if request.method == 'POST':
            # 获取对象
            req = json.loads(request.body)
            global a
            a = req['user_phone']
            # User.objects.filter(user_phone=user_phone).update(head_protrait=obj)
            response['msg'] = a
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
