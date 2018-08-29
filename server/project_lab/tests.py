# -*- coding: utf-8 -*-
import requests
import json
from django.test import TestCase
from django.test import Client
from .utils.yunpian import YunPian

# Create your tests here.
# 验证get请求
# class GetTest(TestCase):


# 验证post请求
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

    def test_get_user_code(self):
        response = self.client.post('/app/get_user_code')
        self.assertEqual(response.status_code, 200)

    def test_manager_login(self):
        response = self.client.post('/app/manager_login')
        self.assertEqual(response.status_code, 200)

    def test_manager_search(self):
        response = self.client.post('/app/back_log_out')
        self.assertEqual(response.status_code, 200)

    def test_manager_change(self):
        response = self.client.post('/app/manager_change')
        self.assertEqual(response.status_code, 200)

    def test_praise(self):
        response = self.client.post('/app/praise')
        self.assertEqual(response.status_code, 200)

    def test_add_reply(self):
        response = self.client.post('/app/add_reply')
        self.assertEqual(response.status_code, 200)

    def test_update_avator(self):
        response = self.client.post('/app/update_avator')
        self.assertEqual(response.status_code, 200)

    def test_update_nickname(self):
        response = self.client.post('/app/update_nickname')
        self.assertEqual(response.status_code, 200)

    def test_get_old_avator(self):
        response = self.client.post('/app/get_old_avator')
        self.assertEqual(response.status_code, 200)

    def test_get_user_information(self):
        response = self.client.post('/app/get_user_information')
        self.assertEqual(response.status_code, 200)

    # def test_search_user(self):
    #     response = self.client.post('/app/search_user')
    #     self.assertEqual(response.status_code, 200)

    # def test_authenticate(self):
    #     response = self.client.post('/app/authenticate')
    #     self.assertEqual(response.status_code, 200)

    # def test_forbid_comment(self):
    #     response = self.client.post('/app/forbid_comment')
    #     self.assertEqual(response.status_code, 200)

    # def test_search_comment(self):
    #     response = self.client.post('/app/search_comment')
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_comment(self):
    #     response = self.client.post('/app/delete_comment')
    #     self.assertEqual(response.status_code, 200)

    # def test_search_order(self):
    #     response = self.client.post('/app/search_order')
    #     self.assertEqual(response.status_code, 200)

    # def test_refund(self):
    #     response = self.client.post('/app/refund')
    #     self.assertEqual(response.status_code, 200)

    def test_get_status(self):
        response = self.client.post('/app/get_status')
        self.assertEqual(response.status_code, 200)

    def test_del_status(self):
        response = self.client.post('/app/del_status')
        self.assertEqual(response.status_code, 200)

    def test_payment(self):
        response = self.client.post('/app/payment')
        self.assertEqual(response.status_code, 200)

    def test_notify(self):
        response = self.client.post('/app/notify')
        self.assertEqual(response.status_code, 200)

    # def test_add_img(self):
    #     response = self.client.post('/app/add_img')
    #     self.assertEqual(response.status_code, 200)

    # def test_add_audi(self):
    #     response = self.client.post('/app/add_audi')
    #     self.assertEqual(response.status_code, 200)

    # def test_set_start_time(self):
    #     response = self.client.post('/app/set_start_time')
    #     self.assertEqual(response.status_code, 200)

    # def test_set_end_time(self):
    #     response = self.client.post('/app/set_end_time')
    #     self.assertEqual(response.status_code, 200)

    # def test_add_course(self):
    #     response = self.client.post('/app/add_course')
    #     self.assertEqual(response.status_code, 200)

    # def test_preview(self):
    #     response = self.client.post('/app/preview')
    #     self.assertEqual(response.status_code, 200)

    def test_account_destroy(self):
        response = self.client.post('/app/account_destroy')
        self.assertEqual(response.status_code, 200)

    def test_show_free_course(self):
        response = self.client.post('/app/show_free_course')
        self.assertEqual(response.status_code, 200)

    def test_show_paying_course(self):
        response = self.client.post('/app/show_paying_course')
        self.assertEqual(response.status_code, 200)

#验证短信发送功能
# class SendMessage(TestCase):
#     def test_yunpian(self):
#         yun_pian = YunPian("264fb31e3ba88e5c55572dd977b2f372")
#         yun_pian.send_sms("6666", "15971181570")
#         self.assertEqual(yun_pian.send_state, '发送成功')
