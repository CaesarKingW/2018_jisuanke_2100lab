from .models import *
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import requests
from .serializer import UserSerializer, ManagerSerializer
from .serializer import Course_pictureSerializer
import os
from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
from urllib.parse import quote_plus
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen
from base64 import decodebytes, encodebytes
from django.conf import settings
from django.contrib.auth import authenticate, login, logout


@require_http_methods(['POST', 'GET'])
def manager_login(request):
    response = {}
    try:
        if request.method == 'POST':
            username = json.loads(request.body)['user']
            password = json.loads(request.body)['password'] + ''
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    response['data'] = 'true'
                else:
                    response['data'] = 'not_active'
            else:
                response['data'] = 'not_exit'
            # info = Manager.objects.get(username=username)
            # info = info.password + ''
            # if password == info:
            #     response['data'] = 'true'
            # else:
            #     response['data'] = 'false'
    except Exception as e:
        response['data'] = 'false'
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def back_logout(request):
    response = {}
    try:
        logout(request)
    except Exception as e:
        response['data'] = 'false'
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse('success', safe=False)


@require_http_methods(['POST', 'GET'])
def manager_change(request):
    response = {}
    try:
        if request.method == 'POST':
            manager = json.loads(request.body)
            info = Manager.objects.get(username=manager['managername'])
            info.Supermanager = manager['super']
            info.Manage_course = manager['course']
            info.Manage_user = manager['user']
            info.Manage_message = manager['message']
            info.Manage_order = manager['order']
            info.save()
            info = ManagerSerializer(info)
            return JsonResponse(info.data)
    except Exception as e:
        response['data'] = 'false'
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def manager_search(request):
    response = {}
    try:
        if request.method == 'POST':
            managername = json.loads(request.body)
            info = Manager.objects.get(username=managername)
            info = ManagerSerializer(info)
            return JsonResponse(info.data)
    except Exception as e:
        response['data'] = 'false'
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def payment(request):
    response = {}
    try:
        if request.method == 'POST':
            id = json.loads(request.body)
            # 订单编号
            orderid = id['orderid']
            # 手机号
            info = User.objects.get(phone_number=id['userphone'])
            phone_number = info
            # 课程编号
            courseid = Course.objects.get(id=id['courseid'])
            # 支付金额
            info = Course.objects.get(id=id['courseid'])
            price = info.price
            # 支付状态
            status = "payment"
            info = Order(
                Order_number=orderid,
                user_phone=phone_number,
                course_id=courseid,
                amount_of_money=price,
                status=status)
            info.save()

            alipay = AliPay(
                appid="2016091800536766",
                app_notify_url="http://192.168.55.33:8000/#/app/notify",
                app_private_key_path=settings.STATIC_ROOT+
                '/private_2048.txt',
                alipay_public_key_path=settings.STATIC_ROOT+
                '/alipay_key_2048.txt',
                debug=True,  # 默认False,
                return_url="http://192.168.55.33:8000/#/CourseShow")
            url = alipay.direct_pay(
                subject="测试订单", out_trade_no=orderid + '', total_amount=price)
            re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(
                data=url)
            # info = ManagerSerializer(re_url)
            return JsonResponse(re_url, safe=False)
    except Exception as e:
        response['data'] = 'false'
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST', 'GET'])
def alipay_get(request):
    # 存放post里面所有的数据
    processed_dict = {}
    try:
        orderid = json.loads(request.body)
        # 查询数据库中订单记录
        info = Order.objects.get(Order_number=orderid)
        courseid = info.course_id.id
        if info.status == 'payment':
            info.status = "completed"
            info.save()
            info = Course.objects.get(id=courseid)
            info.sale_count = info.sale_count + 1
            info.save()
        return JsonResponse("success", safe=False)
    except Exception as e:
        processed_dict['data'] = 'false'
        processed_dict['msg'] = str(e)
        processed_dict['error_num'] = 1
    return JsonResponse(processed_dict)


class AliPay(object):
    """
    支付宝支付接口
    """

    def __init__(self,
                 appid,
                 app_notify_url,
                 app_private_key_path,
                 alipay_public_key_path,
                 return_url,
                 debug=False):
        self.appid = appid
        self.app_notify_url = app_notify_url
        self.app_private_key_path = app_private_key_path
        self.app_private_key = None
        self.return_url = return_url
        with open(self.app_private_key_path) as fp:
            self.app_private_key = RSA.importKey(fp.read())

        self.alipay_public_key_path = alipay_public_key_path
        with open(self.alipay_public_key_path) as fp:
            self.alipay_public_key = RSA.import_key(fp.read())

        if debug is True:
            self.__gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.__gateway = "https://openapi.alipay.com/gateway.do"

    def direct_pay(self,
                   subject,
                   out_trade_no,
                   total_amount,
                   return_url=None,
                   **kwargs):
        biz_content = {
            "subject": subject,
            "out_trade_no": out_trade_no,
            "total_amount": total_amount,
            "product_code": "FAST_INSTANT_TRADE_PAY",
            # "qr_pay_mode":4
        }

        biz_content.update(kwargs)
        data = self.build_body("alipay.trade.page.pay", biz_content,
                               self.return_url)
        return self.sign_data(data)

    def build_body(self, method, biz_content, return_url=None):
        data = {
            "app_id": self.appid,
            "method": method,
            "charset": "utf-8",
            "sign_type": "RSA2",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "version": "1.0",
            "biz_content": biz_content
        }

        if return_url is not None:
            data["notify_url"] = self.app_notify_url
            data["return_url"] = self.return_url

        return data

    def sign_data(self, data):
        data.pop("sign", None)
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        unsigned_string = "&".join(
            "{0}={1}".format(k, v) for k, v in unsigned_items)
        sign = self.sign(unsigned_string.encode("utf-8"))
        ordered_items = self.ordered_data(data)
        quoted_string = "&".join(
            "{0}={1}".format(k, quote_plus(v)) for k, v in ordered_items)

        # 获得最终的订单信息字符串
        signed_string = quoted_string + "&sign=" + quote_plus(sign)
        return signed_string

    def ordered_data(self, data):
        complex_keys = []
        for key, value in data.items():
            if isinstance(value, dict):
                complex_keys.append(key)

        # 将字典类型的数据dump出来
        for key in complex_keys:
            data[key] = json.dumps(data[key], separators=(',', ':'))

        return sorted([(k, v) for k, v in data.items()])

    def sign(self, unsigned_string):
        # 开始计算签名
        key = self.app_private_key
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(SHA256.new(unsigned_string))
        # base64 编码，转换为unicode表示并移除回车
        sign = encodebytes(signature).decode("utf8").replace("\n", "")
        return sign

    def _verify(self, raw_content, signature):
        # 开始计算签名
        key = self.alipay_public_key
        signer = PKCS1_v1_5.new(key)
        digest = SHA256.new()
        digest.update(raw_content.encode("utf8"))
        if signer.verify(digest, decodebytes(signature.encode("utf8"))):
            return True
        return False

    def verify(self, data, signature):
        if "sign_type" in data:
            sign_type = data.pop("sign_type")
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        message = "&".join(u"{}={}".format(k, v) for k, v in unsigned_items)
        return self._verify(message, signature)
