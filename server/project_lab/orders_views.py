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