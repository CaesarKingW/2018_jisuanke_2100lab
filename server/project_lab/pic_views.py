# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
import datetime

@require_http_methods(['POST', 'GET'])
def add_picture(request):
    response={}
    try:
        if request.method == 'POST':
            img = request.FILES['file']
            # courseid = request.body[0]
            # starttime = request.body[1]
            # endtime = request.body[2]
            course = Course.objects.get(id=1)
            start = datetime.timedelta(seconds=15)
            end = datetime.timedelta(seconds=18)
            Course_picture.objects.create(course_id = course, course_picture = img, start_time =start, end_time=end)
            response['msg']='success'
            response['error_num']=0
    except Exception as e:
        response['msg']=str(e)
        response['error_num']=1
    return JsonResponse(response)