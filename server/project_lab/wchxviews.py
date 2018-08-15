from .models import Course, Manager, Operating_history
from django.shortcuts import render, redirect


def course_title(request):
    title = request.POST.get('title')
    course = Course.objects.filter(title=title)
    return render(request, 'course_edit.html', {'course', course})


def Manager_name(request):
    username = request.POST.get('username')
    manager = Manager.objects.filter(username=username)
    return render(request, 'Manage_limits.html', {'manager', manager})


def history(request):
    oprating_history = request.objects.all()[:10]
    return render(request, 'Operating_history.html',
                  {'oprating_history', operating_history})
