# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .serializer import TakesSerializer


# 最新课程学习记录显示在列表末
@require_http_methods(["POST"])
def show_takes(request):
    response = {}
    try:
        # 获取到前端发送回来的数据：用户的电话号码
        req = json.loads(request.body.decode('utf-8'))
        user = User.objects.get(phone_number=req)
        takes = Takes.objects.filter(user_phone=user).order_by('start_time')
        real_takes = []
        for take in takes:
            real_take = TakesSerializer(take)
            real_takes.append(real_take.data)
        response['list'] = real_takes
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def add_or_update_takes(request):
    response = {}
    try:
        req = json.loads(request.body.decode('utf-8'))
        userphone = req['userphone']
        course_id = req['courseid']
        last_study_percent = req['studyPoint']
        user = User.objects.get(phone_number=userphone)
        course = Course.objects.get(id=course_id)
        try:
            take = Takes.objects.get(user_phone=user, course_id=course)
            take.last_study_percent = last_study_percent
            if take.last_study_percent > take.max_study_percent:
                take.max_study_percent = take.last_study_percent
            take.save()
        except:
            take = Takes.objects.create(user_phone=user, course_id=course)
            course.view_count = course.view_count + 1
            course.save()
            take.last_study_percent = last_study_percent
            if take.last_study_percent > take.max_study_percent:
                take.max_study_percent = take.last_study_percent
            take.save()
        response['msg'] = 'success'
        response['errornum'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['errornum'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def add_new_take(request):
    response = {}
    try:
        req = json.loads(request.body.decode('utf-8'))
        userphone = req['userphone']
        course_id = req['courseid']
        startPoint = req['beginPoint']
        user = User.objects.get(phone_number=userphone)
        course = Course.objects.get(id=course_id)
        try:
            take = Takes.objects.get(user_phone=user, course_id=course)
            response['startPoint'] = take.start_time
            response['breakPoint'] = take.last_study_percent
        except:
            take = Takes.objects.create(
                user_phone=user, course_id=course, start_time=startPoint)
            response['startPoint'] = take.start_time
            response['breakPoint'] = take.last_study_percent
            course.view_count = course.view_count + 1
            course.save()
        response['msg'] = 'success'
        response['errornum'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['errornum'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def set_burn(request):
    response = {}
    try:
        req = json.loads(request.body.decode('utf-8'))
        userphone = req['userphone']
        course_id = req['courseid']
        user = User.objects.get(phone_number=userphone)
        course = Course.objects.get(id=course_id)
        take = Takes.objects.get(user_phone=user, course_id=course)
        take.burn = True
        take.save()
        response['msg'] = 'success'
        response['errornum'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['errornum'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def get_burn_status(request):
    response = {}
    try:
        req = json.loads(request.body.decode('utf-8'))
        userphone = req['userphone']
        course_id = req['courseid']
        try:
            user = User.objects.get(phone_number=userphone)
            course = Course.objects.get(id=course_id)
            take = Takes.objects.get(user_phone=user, course_id=course)
            response['status'] = take.burn
        except:
            response['status'] = False
        response['msg'] = 'success'
        response['errornum'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['errornum'] = 1

    return JsonResponse(response)


@require_http_methods(["POST"])
def add_share(request):
    response = {}
    try:
        req = json.loads(request.body.decode('utf-8'))
        receiver = req['receiver']
        course_id = req['courseid']
        presenter_number = req['presenter']
        try:
            presenter = User.objects.get(phone_number=presenter_number)
            try:
                Share.objects.get(
                    presenter=presenter,
                    receiver=receiver,
                    course_id=course_id,
                )
                response['status'] = True
            except:
                Share.objects.create(
                    presenter=presenter,
                    receiver=receiver,
                    course_id=course_id,
                )
                response['status'] = True
        except:
            response['status'] = False
        response['receiver'] = receiver
        response['msg'] = 'success'
        response['errornum'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['errornum'] = 1

    return JsonResponse(response)
