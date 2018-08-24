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


@require_http_methods(['POST', 'GET'])
def add_picture(request):
    response = {}
    try:
        if request.method == 'POST':
            # 获取对象
            obj = request.FILES.get('file')
            # response['object'] = obj
            # response['objec'] = 1
            # 上传文件的文件名
            # print(obj.name)
            # f = open(
            #     os.path.join(BASE_DIR, 'project_lab', 'static', 'media',
            #                  'course_picture', obj.name), 'wb')
            # for chunk in obj.chunks():
            #     f.write(chunk)
            #     f.close()
            course_id = Course.objects.get(id=1)
            new_picture = Course_picture(
                course_id=course_id,
                course_picture=obj,
                start_time=datetime.timedelta(seconds=15),
                end_time=datetime.timedelta(seconds=18))
            new_picture.save()
    except Exception as e:
        print('error')
    return HttpResponse(obj.name)


@require_http_methods(['GET'])
def show_picture(request):
    response = {}
    try:
        if request.method == 'GET':
            course = Course_picture.objects.filter(id=1)
            # img = course.course_picture
            response['img'] = json.loads(serializers.serialize("json", course))
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
