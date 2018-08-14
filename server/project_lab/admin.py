from django.contrib import admin
from .models import User, Manager, Operating_history, Course, Course_picture, Takes, Order
# Register your models here.
admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Operating_history)
admin.site.register(Course)
admin.site.register(Course_picture)
admin.site.register(Takes)
admin.site.register(Order)
