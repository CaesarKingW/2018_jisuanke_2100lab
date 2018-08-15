from .models import Course
from django.shortcuts import render, redirect
def course_title(request):
  title = request.POST.get('title')
  course = Course.objects.filter(title=title)
  return render(request,'course_edit.html', {'course',course})
def Manager_name(request):
  username = request.POST.get('username')
  manager = Manager.objects.filter(username = username)
  return render(request,'Manage_limits.html', {'manager', manager})
