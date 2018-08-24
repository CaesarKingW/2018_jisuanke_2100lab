# -*- coding: utf-8 -*-
import requests
import json
from django.test import TestCase
from django.test import Client
from .utils.yunpian import YunPian



# Create your tests here.
#验证get请求
# class GetTest(TestCase):


#验证post请求
class PostTest(TestCase):
    def test_add_message(self):
        response = self.client.post('/app/add_message')
        self.assertEqual(response.status_code, 200)

    def test_get_code_post(self):
        response = self.client.post('/app/get_code_post')
        self.assertEqual(response.status_code, 200)

    def test_register_new_user(self):
        response = self.client.post('/app/register_new_user')
        self.assertEqual(response.status_code, 200)

    def test_show_reply(self):
        response = self.client.post('/app/show_reply')
        self.assertEqual(response.status_code, 200)

    def test_show_message(self):
        response = self.client.post('/app/show_message')
        self.assertEqual(response.status_code, 200)

#验证短信发送功能
class SendMessage(TestCase):
    def test_yunpian(self):
        yun_pian = YunPian("264fb31e3ba88e5c55572dd977b2f372")
        yun_pian.send_sms("6666", "15971181570")
        self.assertEqual(yun_pian.send_state, '发送成功')
