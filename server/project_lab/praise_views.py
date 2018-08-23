# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse


@require_http_methods(["POST"])
def praise_record(request):
    response = {}
    try:
        req = json.loads(request.body)
        message_id = req['message_id']
        user_phone = req['user_phone']
        user = User.objects.get(phone_number=user_phone)
        message = Message.objects.get(id=message_id)
        praise_record = Praise.objects.filter(
            message_id=message, user_phone=user)
        if praise_record.count() == 0:
            response['has_praise'] = False
            Praise.objects.create(message_id=message, user_phone=user)
            Message.objects.filter(id=message_id).update(
                praise_count=message.praise_count + 1)
        else:
            response['has_praise'] = True
            Praise.objects.filter(message_id=message, user_phone=user).delete()
            Message.objects.filter(id=message_id).update(
                praise_count=message.praise_count - 1)
        response['count'] = praise_record.count()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)