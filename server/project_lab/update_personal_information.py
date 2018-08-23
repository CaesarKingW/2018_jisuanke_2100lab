# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
import datetime
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

a = ''


@require_http_methods(['POST', 'GET'])
def update_avator(request):
    response = {}
    try:
        if request.method == 'POST':
            # 获取对象
            b = request.FILES.get('file')
            new = User.objects.get(phone_number=a)
            new.head_protrait=b
            new.save()
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
            response['msg'] = a
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST'])
def update_nickname(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            user = User.objects.get(phone_number=req['phone_number'])
            user.user_name = req['nickname']
            user.save()
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
