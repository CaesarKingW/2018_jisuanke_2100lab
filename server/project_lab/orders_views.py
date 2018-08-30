# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .serializer import OrderSerializer
import random
import math


def ran_number():
    return random.randint(0, 9)


def createCode():
    global code
    code = ''
    codeLength = 16
    random = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # 随机数
    for i in range(codeLength):
        index = ran_number()
        code = code + random[index]
    return code


# 最新订单记录显示在上端
@require_http_methods(["POST"])
def show_orders(request):
    response = {}
    try:
        # 获取到前端发送回来的数据：用户的电话号码
        req = json.loads(request.body.decode('utf-8'))
        user = User.objects.get(phone_number=req)
        orders = Order.objects.filter(user_phone=user).order_by('-create_at')
        real_orders = []
        for order in orders:
            real_order = OrderSerializer(order)
            real_orders.append(real_order.data)
        response['list'] = real_orders
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# 获取支付状态，支付完成返回TRUE，否则返回false
@require_http_methods(["POST"])
def get_order_payment(request):
    response = {}
    try:
        # 获取到前端发送回来的数据：用户的电话号码和课程id
        req = json.loads(request.body.decode('utf-8'))
        phone_number = req['phone_number']
        course_id = req['course_id']
        user = User.objects.get(phone_number=phone_number)
        course = Course.objects.get(id=course_id)
        try:
            orders = Order.objects.filter(user_phone=user, course_id=course)
            for order in orders:
                if order.status == "已支付":
                    response['order_status'] = True
                    return JsonResponse(response)
            response['order_status'] = False
        except:
            response['order_status'] = False
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# 使用奖励金支付，创建订单，课程销量加加，奖励金减减
@require_http_methods(["POST"])
def award_pay(request):
    response = {}
    try:
        # 获取到前端发送回来的数据：用户的电话号码和课程id
        req = json.loads(request.body.decode('utf-8'))
        phone_number = req['userphone']
        course_id = req['courseid']
        left = req['userAward']
        price = req['price']
        user = User.objects.get(phone_number=phone_number)
        course = Course.objects.get(id=course_id)
        try:
            Order.objects.get(user_phone=user, course_id=course, status="已支付")
        except:
            Order.objects.create(
                Order_number=createCode(),
                user_phone=user,
                course_id=course,
                amount_of_money=price,
                status="已支付")
            try:
                share = Share.objects.get(receiver=phone_number, course_id=course_id)
                award_plus = math.floor(course.price * course.share_rate)
                presenter = share.presenter
                presenter.welfare = presenter.welfare + award_plus
                presenter.save()
                response['add_award'] = 'success'
            except:
                response['add_award'] = 'fail'
        user.welfare = left
        user.save()
        course.sale_count = course.sale_count + 1
        course.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)