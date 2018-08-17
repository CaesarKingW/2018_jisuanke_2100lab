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
