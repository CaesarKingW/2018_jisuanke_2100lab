from .models import Course, Manager, Operating_history
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
import requests


def search_managename(request):
    response = {}
    username = request.body
    manager = Manager.objects.get(username=username)
    response['manager'] = json.loads(serializers.serialize('json', manager))
    return JsonResponse(response)


def search_course(request):
    response = {}
    title = request.body
    course = Course.objects.get(title=title)
    response['course'] = json.loads(serializers.serialize('json', course))
    return JsonResponse(response)


def history(request):
    response = {}
    histories = Operating_history.objects.all()
    response['list'] = json.loads(serializers.serialize('json', histories))
    return JsonResponse(response)
