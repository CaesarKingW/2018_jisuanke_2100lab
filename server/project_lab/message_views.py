# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .utils.yunpian import YunPian


@require_http_methods(["POST"])
def show_message(request):
    response = {}
    try:
        req = json.loads(request.body)
        course_id = Course.objects.get(id=req)
        messages = Message.objects.filter(course_id=course_id)
        response['list'] = json.loads(serializers.serialize("json", messages))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def add_message(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            user_phone = User.objects.get(phone_number=req['user_phone'])
            course_id = Course.objects.get(id=req['course_id'])
            Message.objects.create(
                user_phone=user_phone,
                course_id=course_id,
                content=req['content'])
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def show_reply(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            message = Message.objects.get(id=req)
            replies = Reply.objects.filter(message_id=message)
            response['list'] = json.loads(
                serializers.serialize("json", replies))
            response['msg'] = 'wangkang'
            response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
