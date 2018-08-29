# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from project_lab.models import *
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers
from django.http import JsonResponse
from .serializer import OrderSerializer


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
