# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
# from .apps import AppnameConfig
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse


@require_http_methods(['POST', 'GET'])
def register_new_user(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            # yun_pian = YunPian("264fb31e3ba88e5c55572dd977b2f372")
            # yun_pian.send_sms(req['checkCode'], req['phone_number'])
            User.objects.create(phone_number=req)
            response['num'] = req
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)