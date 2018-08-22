# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse

@require_http_methods(['POST', 'GET'])
def account_destroy(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body)
            current_user = User.objects.get(phone_number=req)
            current_user.is_active = False
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)