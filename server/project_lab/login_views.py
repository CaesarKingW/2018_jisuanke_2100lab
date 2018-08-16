# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# from .apps import AppnameConfig
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .utils.yunpian import YunPian
import random


def ran_number():
    return random.randint(1000, 9999)


@require_http_methods(['POST', 'GET'])
def get_code_post(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            yun_pian = YunPian("264fb31e3ba88e5c55572dd977b2f372")
            yun_pian.send_sms(ran_number(), req)
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)