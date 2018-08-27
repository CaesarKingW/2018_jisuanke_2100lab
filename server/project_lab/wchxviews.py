from .models import *
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import requests


def search_managename(request):
    response = {}
    username = request.body.decode('utf-8')
    manager = Manager.objects.get(username=username)
    response['manager'] = json.loads(serializers.serialize('json', manager))
    return JsonResponse(response)


def search_course(request):
    response = {}
    title = request.body.decode('utf-8')
    course = Course.objects.get(title=title)
    response['course'] = json.loads(serializers.serialize('json', course))
    return JsonResponse(response)


def history(request):
    response = {}
    histories = Operating_history.objects.all()
    response['list'] = json.loads(serializers.serialize('json', histories))
    return JsonResponse(response)


def get_status(request):
    response = {}
    try:
        if request.method == 'POST':
            user = User.objects.get(
                phone_number=request.session['user'].phone_number)
            request.session['user'] = user
            the_user = User.objects.filter(
                phone_number=request.session['user'].phone_number)
            response['is_login'] = request.session['is_login']
            response['list'] = json.loads(serializers.serialize("json", the_user))
    except:
        response['msg'] = 'fail'
    return JsonResponse(response)


def del_status(request):
    response = {}
    try:
        if request.method == 'POST':
            request.session['is_login'] = False
            response['is_login'] = request.session['is_login']
            response['username'] = request.session['user'].user_name
            response['phonenumber'] = request.session['user'].phone_number
            del request.session['is_login']
            del request.session['user']
    except:
        response['msg'] = 'fail'
    return JsonResponse(response)
