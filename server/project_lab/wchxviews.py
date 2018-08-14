from .models import Course
from django.shortcuts import render, redirect
def course_title(request):
  title = request.POST.get('title')
  course = Course.object.filter(title=title)
  return render(request,'course_edit.html')
