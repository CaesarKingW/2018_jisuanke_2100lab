# -*- coding: utf-8 -*-
import requests
import json


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【王康王康】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        print(re_dict)
