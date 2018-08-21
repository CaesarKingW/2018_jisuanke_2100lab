from django.core import serializers
from .models import User, Message, Course, Order, Course_picture
from .models import Operating_history
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import json
from rest_framework.response import Response
from .serializer import UserSerializer, MessageSerializer, OrderSerializer, CourseSerializer, Course_pictureSerializer


@require_http_methods(['POST'])
def search_user(request):

    phone_number = json.loads(request.body)
    res = {}
    try:
        user = User.objects.get(phone_number=phone_number)
        res['is_null'] = False
        user = UserSerializer(user)
        res['user_info'] = user.data
    except:
        res['is_null'] = True
        return JsonResponse(res)
    return JsonResponse(res)


@require_http_methods(['POST'])
def authenticate(request):
    phone_number = json.loads(request.body)
    user = User.objects.get(phone_number=phone_number)
    if (user.Is_teacher is False):
        user.Is_teacher = True
        user.save()
    else:
        user.Is_teacher = False
        user.save()
    # Operating_history.objects.create()
    user = UserSerializer(user)
    # print(request.user)
    return JsonResponse(user.data)


@require_http_methods(['POST'])
def forbid_comment(request):
    phone_number = json.loads(request.body)
    user = User.objects.get(phone_number=phone_number)
    if (user.Can_comment is False):
        user.Can_comment = True
        user.save()
    else:
        user.Can_comment = False
        user.save()
    # Operating_history.objects.create()
    user = UserSerializer(user)
    return JsonResponse(user.data)


@require_http_methods(['POST'])
def close_account(request):
    response = {}
    try:
        phone_number = request.body
        User.objects.get(phone_number=phone_number)
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['POST'])
def search_comment(request):
    phone_number = json.loads(request.body)
    response = {}
    response['if_user'] = True
    response['if_comment'] = True
    try:
        user = User.objects.get(phone_number=phone_number)
        messages = Message.objects.filter(user_phone=user)
        if messages.count() == 0:
            response['if_comment'] = False
            return JsonResponse(response)
        else:
            real_messages = []
            for message in messages:
                real_message = MessageSerializer(message)
                real_messages.append(real_message.data)
            response['messages'] = real_messages
    except:
        response['if_user'] = False
        return JsonResponse(response)
    return JsonResponse(response)


@require_http_methods(['POST'])
def delete_comment(request):
    phone_number = json.loads(request.body)['phone_number']
    message_id = json.loads(request.body)['message_id']
    response = {}
    response['if_user'] = True
    m = Message.objects.get(id=message_id)
    m.delete()
    n = User.objects.get(phone_number=phone_number)
    messages = Message.objects.filter(user_phone=n)
    response['if_comment'] = True
    if messages.count() == 0:
        response['if_comment'] = False
        return JsonResponse(response)
    real_messages = []
    for message in messages:
        real_message = MessageSerializer(message)
        real_messages.append(real_message.data)
    response['messages'] = real_messages
    return JsonResponse(response)


@require_http_methods(['POST'])
def search_order(request):
    order_number = json.loads(request.body)
    response = {}
    response['if_order'] = True
    try:
        order = Order.objects.get(Order_number=order_number)
        order = OrderSerializer(order)
        response['order_info'] = order.data
    except:
        response['if_order'] = False
        return JsonResponse(response)
    return JsonResponse(response)


@require_http_methods(['POST'])
def refund(request):
    order_number = json.loads(request.body)
    order = Order.objects.get(Order_number=order_number)
    phone_number = order.user_phone
    user = User.objects.get(phone_number=phone_number)
    w = user.welfare
    user.welfare = w + order.amount_of_money
    user.save()
    order.status = '已退款'
    order.save()
    order = OrderSerializer(order)
    return JsonResponse(order.data)


# @require_http_methods(['POST'])
# def search_course(request):
#     course_title = json.loads(request.body)
#     response={}
#     courses = Course.objects.filter(title=course_title)
#     if courses.count() == 0:
#         response['if_courses'] = False
#     else:
#         response['if_courses'] = True
#         real_courses =  []
#         pictures_by_course = {}
#         for course in courses:
#             pictures = Course_picture.filter(course_id=course)
#             if pictures.count() == 0:
#                 pictures_by_course['course.id'] = 0
#             else:
#                 pictures_by_course['course.id'] = []
#                 for picture in pictures:
#                     real_picture = Course_pictureSerializer(picture)
#                     pictures_by_course['course.id'].append(real_picture.data)
#             real_course = CourseSerializer(course)
#             real_courses.append(real_course.data)
