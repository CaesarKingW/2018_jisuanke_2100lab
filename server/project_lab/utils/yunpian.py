# -*- coding: utf-8 -*-
import requests
import json


class YunPian(object):
    send_state = ""


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
        self.send_state = re_dict['msg']
        print(re_dict)
    
if __name__=="__main__":
      yun_pian = YunPian("264fb31e3ba88e5c55572dd977b2f372")
      yun_pian.send_sms("2222", "15971181570")
