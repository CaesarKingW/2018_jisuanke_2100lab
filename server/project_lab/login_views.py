# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .utils.yunpian import YunPian
import random

code = ''
user_phone = ''


def ran_number():
    return random.randint(0, 35)


def createCode():
    global code
    code = ''
    codeLength = 4
    random = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]  # 随机数
    for i in range(codeLength):
        index = ran_number()
        code = code + random[index]


@require_http_methods(['POST', 'GET'])
def get_code_post(request):
    response = {}
    try:
        if request.method == 'POST':
            global code
            global user_phone
            createCode()
            req = json.loads(request.body)
            user_phone = req
            yun_pian = YunPian("264fb31e3ba88e5c55572dd977b2f372")
            yun_pian.send_sms(code, req)
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def get_user_code(request):
    response = {}
    try:
        if request.method == 'POST':
            global code
            global user_phone
            #获取用户输入的验证码
            req = json.loads(request.body)
            userPhone = req['phone_number']
            userCode = req['code']
            if userPhone == user_phone and userCode == code:
                response['status'] = True
                code = ''
                user_phone = ''
            else:
                response['status'] = False
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
