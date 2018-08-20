from .models import Course, Manager, Operating_history, User
from django.views.generic.base import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.forms.models import model_to_dict
import json
import requests
from .serializer import UserSerializer


# @require_http_methods(['POST', 'GET'])
# def user_comment1(request):
#   info = User.objects.filter(user_name="lisi")
#     #response={}
#     #response = Manager.objects.get()
#     #response = json.loads(serializers.serialize('json', User.objects.get(phone_number="11122223333")))
#     #manager = Manager.objects.get(username=username)
#     #response['manager'] = json.loads(serializers.serialize('json', manager))
#   response=json.loads(serializers.serialize('json',info))
#   return JsonResponse(response, safe=False)



@require_http_methods(['POST', 'GET'])
def user_comment(request):
  phone_number=json.loads(request.body)
  info = User.objects.get(phone_number=phone_number)
  info = UserSerializer(info)
  return JsonResponse(info.data)


@require_http_methods(['POST', 'GET'])
def user_login(request):
    response = {}
    try:
        if request.method == 'POST':
            username = json.loads(request.body)['user']
            password = json.loads(request.body)['password']
            info=Manager.objects.get(username=username)
            info=info.password
            #response = json.loads(
            #    serializers.serialize("json", username))
            if password==info:
                response['data']='true'
            else: response['data']='false'
    except Exception as e:
        response['data']='false'
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# def user_comment2(request):
#   # phonenumber = str(request.POST.get("phone_number"))
#   # info = User.objects.filter(phone_number=phonenumber)
#   # response=json.loads(serializers.serialize('json',info))
#   # return JsonResponse(response, safe=False)
#   req = json.loads(request.body)
#   return JsonResponse()
