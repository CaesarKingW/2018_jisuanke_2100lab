from django.core import serializers
from .models import User, Message, Course, Order, Course_picture, Manager
from .models import Operating_history
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import json
from rest_framework.response import Response
from .serializer import UserSerializer, ManagerSerializer
from .serializer import MessageSerializer, ReplySerializer
from .serializer import OrderSerializer, CourseSerializer
from .serializer import Course_pictureSerializer, Operating_historySerializer
from django.contrib import auth
import string


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
        manager_username = request.user.username
        manager = Manager.objects.get(username=manager_username)
        operating_history = Operating_history(
            manager_username=manager,
            operate_type="认证用户",
            object_type="用户(手机号：" + phone_number + ")")
    else:
        user.Is_teacher = False
        user.save()
        operating_history = Operating_history(
            manager_username=manager,
            operate_type="取消用户认证",
            object_type="用户(手机号：" + phone_number + ")")
    user = UserSerializer(user)

    operating_history.save()
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
    user = UserSerializer(user)
    manager_username = request.user.username
    manager = Manager.objects.get(username=manager_username)
    operating_history = Operating_history(
        manager_username=manager,
        operate_type="禁言用户",
        object_type="用户：(手机号：" + phone_number + ")")
    operating_history.save()
    return JsonResponse(user.data)


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
    operator = Manager.objects.get(username=request.user.username)
    operating_history = Operating_history(
        manager_username=operator,
        operate_type="删除留言",
        object_type="留言（留言用户：" + m.user_phone.phone_number + ";留言内容：" +
        m.content + ";留言时间：" + m.created_at + ";留言课程：" + m.course_id)
    operating_history.save()
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
    res = {}
    order = Order.objects.get(Order_number=order_number)
    phone_number = order.user_phone
    user = User.objects.get(phone_number=phone_number)
    w = user.welfare
    user.welfare = w + order.amount_of_money
    user.save()
    order.status = '已退款'
    order.save()
    res['manager_username'] = request.user.username
    manager = Manager.objects.get(username=request.user.username)
    operating_history = Operating_history(
        manager_username=manager,
        operate_type='办理退款',
        object_type='订单（订单号：' + order_number + ')')
    operating_history.save()
    order = OrderSerializer(order)
    res['order'] = order.data
    return JsonResponse(res)


@require_http_methods(['POST'])
def add_course(request):
    res = {}
    title = json.loads(request.body)['title']
    brief_intro = json.loads(request.body)['brief_intro']
    res['msg'] = (title != "" and brief_intro != "")
    if res['msg']:
        course = Course(title=title, brief_introduction=brief_intro)
        course.save()
        course = CourseSerializer(course)
        res['course'] = course.data
    return JsonResponse(res)


@require_http_methods(['POST'])
def add_img(request):
    course_id = request.POST.get('course_id')
    duration = float(request.POST.get('duration'))
    course = Course.objects.get(id=course_id)
    course.course_duration = duration
    course.save()
    file_obj = request.FILES.get('file')
    course_picture = Course_picture(course_id=course, course_picture=file_obj)
    course_picture.save()
    course_picture = Course_pictureSerializer(course_picture)
    return JsonResponse(course_picture.data)


@require_http_methods(['POST'])
def add_audi(request):
    file_obj = request.FILES.get('file')
    course_id = request.POST.get('course_id')
    course = Course.objects.get(id=course_id)
    course.audio = file_obj
    course.save()
    course = CourseSerializer(course)
    return JsonResponse(course.data)


@require_http_methods(['POST'])
def set_start_time(request):
    start_time = json.loads(request.body)['start_time']
    pic_id = json.loads(request.body)['pic_id']
    pic = Course_picture.objects.get(id=pic_id)
    pic.start_time = start_time
    pic.save()
    pic = Course_pictureSerializer(pic)
    return JsonResponse(pic.data)


@require_http_methods(['POST'])
def set_end_time(request):
    end_time = json.loads(request.body)['end_time']
    pic_id = json.loads(request.body)['pic_id']
    pic = Course_picture.objects.get(id=pic_id)
    pic.end_time = end_time
    pic.save()
    pic = Course_pictureSerializer(pic)
    return JsonResponse(pic.data)


@require_http_methods(['POST'])
def preview(request):
    course_id = json.loads(request.body)['course_id']
    course = Course.objects.get(id=course_id)
    course_pictures = Course_picture.objects.filter(course_id=course)
    course = CourseSerializer(course)
    real_course_pictures = []
    for course_picture in course_pictures:
        real_course_picture = Course_pictureSerializer(course_picture)
        real_course_pictures.append(real_course_picture.data)
    response = {}
    response['course'] = course.data
    response['pictures'] = real_course_pictures
    return JsonResponse(response)


@require_http_methods(['POST'])
def supplement_course_information(request):
    response = {}
    course = Course.objects.get(id=request.POST.get('id'))
    course.whole_introduction = request.FILES.get('whole_introduction')
    course.Cover_picture = request.FILES.get('Cover_picture')
    course.Is_destroy = buer(request.POST.get('Is_destroy'))
    course.price = float(request.POST.get('price'))
    course.can_comment = buer(request.POST.get('can_comment'))
    if buer(request.POST.get('Is_destroy')) is True:
        course.distroy_time = float(request.POST.get('distroy_time'))
    if float(request.POST.get('price')) > 0:
        course.share_rate = float(request.POST.get('share_rate')) / 100
    course.save()
    operating_history = Operating_history(
        manager_username=request.user,
        operate_type="新建课程",
        object_type="课程（课程id：" + str(course.id) + ")")
    operating_history.save()
    course = CourseSerializer(course)
    response['course'] = course.data
    return JsonResponse(course.data)


@require_http_methods(['POST'])
def search_manager(request):
    username = json.loads(request.body)
    res = {}
    res['if_exist'] = True
    try:
        manager = Manager.objects.get(username=username)
        res['if_exist'] = True
        manager = ManagerSerializer(manager)
        res['manager'] = manager.data
    except:
        res['if_exist'] = False
    return JsonResponse(res)


@require_http_methods(['POST'])
def Modify(request):
    username = json.loads(request.body)['username']
    Manage_course = json.loads(request.body)['Manage_course']
    Manage_user = json.loads(request.body)['Manage_user']
    Manage_message = json.loads(request.body)['Manage_message']
    Manage_order = json.loads(request.body)['Manage_order']
    manager = Manager.objects.get(username=username)
    manager.Manage_course = Manage_course
    manager.Manage_user = Manage_user
    manager.Manage_message = Manage_message
    manager.Manage_order = Manage_order
    manager.save()
    operator = request.user.username
    operator = Manager.objects.get(username=operator)
    operating_history = Operating_history(
        manager_username=operator,
        operate_type='修改权限',
        object_type='管理员(用户名：' + username + ')')
    operating_history.save()
    manager = ManagerSerializer(manager)
    return JsonResponse(manager.data)


@require_http_methods(['POST'])
def backstage_login(request):
    username = json.loads(request.body)['username']
    password = json.loads(request.body)['password']
    res = {}
    try:
        manager = Manager.objects.get(username=username)
        res['if_exist'] = True
        manager = auth.authenticate(username=username, password=password)
        if manager is not None:
            res['pw_right'] = True
            auth.login(request, manager)
            request.session['user'] = username
            request.session['mis_login'] = True
        else:
            res['pw_right'] = False
    except:
        res['if_exist'] = False
    return JsonResponse(res)


@require_http_methods(['POST'])
def backstage_register(request):
    username = json.loads(request.body)['username']
    password = json.loads(request.body)['password']
    res = {}
    manager = Manager.objects.create_user(username=username, password=password)
    manager.save()
    return JsonResponse(res)


@require_http_methods(['POST'])
def check(request):
    username = json.loads(request.body)['username']
    res = {}
    try:
        manager = Manager.objects.get(username=username)
        res['if_exist'] = True
        manager = ManagerSerializer(manager)
        res['manager_info'] = manager.data
    except:
        res['if_exist'] = False
    return JsonResponse(res)


@require_http_methods(['POST'])
def get_mstatus(request):
    response = {}
    try:
        response['mis_login'] = request.session['mis_login']
        if request.session['mis_login'] is True:
            response['user'] = request.session['user']
        try:
            manager = Manager.objects.get(username=request.session['user'])
            manager = ManagerSerializer(manager)
            response['test'] = True
            response['manager'] = manager.data
        except:
            response['test'] = False
        # if request.session['mis_login'] is True:
        #     manager = Manager.objects.get(username=request.session['user'])
        #     response['manager'] = manager
    except:
        response['msg'] = 'fail'
    return JsonResponse(response)


@require_http_methods(['POST'])
def search_history(request):
    response = {}
    response['user'] = request.session['user']
    username = request.session['user']
    manager = Manager.objects.get(username=username)
    historys = Operating_history.objects.filter(manager_username=manager)
    response['num'] = historys.count()
    real_historys = []
    for history in historys:
        real_history = Operating_historySerializer(history)
        real_historys.append(real_history.data)
    response['history'] = real_historys
    return JsonResponse(response)


@require_http_methods(['POST'])
def search_course(request):
    response = {}
    title = json.loads(request.body)
    courses = Course.objects.filter(title__contains=title)
    response['num'] = courses.count()
    if courses.count() > 0:
        real_courses = []
        for course in courses:
            course = CourseSerializer(course)
            real_courses.append(course.data)
        response['courses'] = real_courses
    return JsonResponse(response)


@require_http_methods(['POST'])
def delete_course(request):
    response = {}
    id = json.loads(request.body)
    course = Course.objects.get(id=id)
    course.delete()
    response['msg'] = 'success'
    return JsonResponse(response)


@require_http_methods(['POST'])
def search_one_course(request):
    response = {}
    id = json.loads(request.body)
    course = Course.objects.get(id=id)
    course = CourseSerializer(course)
    response['course'] = course.data
    request.session['id'] = id
    response['id'] = request.session['id']
    return JsonResponse(response)


@require_http_methods(['POST'])
def test(request):
    response = {}
    response['msg'] = float(request.POST.get('test'))
    return JsonResponse(response)


def buer(s):
    if s == "true":
        return True
    if s == "false":
        return False


@require_http_methods(['POST'])
def editCourse(request):
    response = {}
    course = Course.objects.get(id=request.POST.get('id'))
    course.title = request.POST.get('title')
    course.brief_introduction = request.POST.get('brief_introduction')
    course.whole_introduction = request.FILES.get('whole_introduction')
    course.Cover_picture = request.FILES.get('Cover_picture')
    course.Is_destroy = buer(request.POST.get('Is_destroy'))
    course.price = float(request.POST.get('price'))
    course.can_comment = buer(request.POST.get('can_comment'))
    if buer(request.POST.get('Is_destroy')) is True:
        course.distroy_time = float(request.POST.get('distroy_time'))
    if float(request.POST.get('price')) > 0:
        course.share_rate = float(request.POST.get('share_rate')) / 100
    course.save()
    operating_history = Operating_history(
        manager_username=request.user,
        operate_type="编辑课程",
        object_type="课程（课程id：" + str(course.id) + ")")
    operating_history.save()
    course = CourseSerializer(course)
    response['course'] = course.data
    return JsonResponse(response)
