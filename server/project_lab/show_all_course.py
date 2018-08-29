# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse


@require_http_methods(['POST', 'GET'])
def show_free_course(request):
    response = {}
    try:
        if request.method == 'GET':
            course = Course.objects.filter(price=0).order_by('-created_at')
            response['list'] = json.loads(
                serializers.serialize("json", course))
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def show_paying_course(request):
    response = {}
    try:
        if request.method == 'GET':
            course = Course.objects.exclude(price=0).order_by('-created_at')
            response['list'] = json.loads(
                serializers.serialize("json", course))
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def get_specified_course(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body.decode('utf-8'))
            try:
                temp = Course.objects.get(id=req)
                course = Course.objects.filter(id=req)
                response['list'] = json.loads(
                    serializers.serialize("json", course))
                response['exist'] = True
            except:
                response['exist'] = False
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
