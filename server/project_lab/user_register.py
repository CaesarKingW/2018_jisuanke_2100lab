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
            req = json.loads(request.body.decode('utf-8'))
            request.session['is_login'] = True
            try:
                user = User.objects.get(phone_number=req)
            except:
                User.objects.create(phone_number=req)
                user = User.objects.get(phone_number=req)
            request.session['user'] = user
            response['is_login'] = request.session['is_login']
            response['num'] = req
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
