# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .serializer import MessageSerializer, ReplySerializer


# 最高点赞数留言显示在顶端
@require_http_methods(["POST"])
def show_message(request):
    response = {}
    try:
        req = json.loads(request.body.decode('utf-8'))
        course_id = Course.objects.get(id=req)
        messages = Message.objects.filter(
            course_id=course_id, exists=True).order_by('-created_at')
        real_messages = []
        for message in messages:
            real_message = MessageSerializer(message)
            real_messages.append(real_message.data)
        response['list'] = real_messages
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
            req = json.loads(request.body.decode('utf-8'))
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


#最新回复显示在留言的最下端
@require_http_methods(["POST"])
def show_reply(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body.decode('utf-8'))
            message = Message.objects.get(id=req)
            replies = Reply.objects.filter(
                message_id=message).order_by('created_at')
            real_replies = []
            for reply in replies:
                real_reply = ReplySerializer(reply)
                real_replies.append(real_reply.data)
            response['list'] = real_replies
            response['msg'] = 'success'
            response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def add_reply(request):
    response = {}
    try:
        if request.method == 'POST':
            req = json.loads(request.body.decode('utf-8'))
            user_phone = User.objects.get(phone_number=req['user_phone'])
            message_id = Message.objects.get(id=req['message_id'])
            Reply.objects.create(
                user_phone=user_phone,
                message_id=message_id,
                content=req['content'])
            response['msg'] = 'success'
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)
