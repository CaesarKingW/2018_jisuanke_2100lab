# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .utils.yunpian import YunPian


@require_http_methods(["GET"])
def show_message(requset):
    response = {}
    try:
        messages = Message.objects.filter()
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
            user_name = User.objects.get(phone_number='15600558989')
            course_id = Course.objects.get(id=1)
            Message.objects.create(
                user_name=user_name, course_id=course_id, content=req)
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["POST", "GET"])
# def show_reply(request):
#     response = {}
#     try:
#         if request.method == 'POST':
#             req = json.loads(request.body)
#             user_name = User.objects.get(phone_number='15600558989')
#             course_id = Course.objects.get(id=1)
#             Message.objects.create(
#                 user_name=user_name, course_id=course_id, content=req)
#             response['msg'] = 'success'
#             response['error_num'] = 0
#     except Exception as e:
#         response['msg'] = str(e)
#         response['error_num'] = 1

#     return JsonResponse(response)
def show_reply(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            message = Message.objects.get(message_id=req)
            replies = Reply.objects.filter(message_id=message)
            response['list'] = json.loads(
                serializers.serialize("json", replies))
            response['msg'] = 'wangkang'
            response['error_num'] = 0
        if request.method == 'GET':
            if(message != ''):
                replies = Reply.objects.filter(message_id=message)
                response['list'] = json.loads(serializers.serialize("json", replies))
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
