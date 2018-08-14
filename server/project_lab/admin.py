from django.contrib import admin
from .models import User, Manager, Operating_history, Course, Course_picture
# Register your models here.
admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Operating_history)
admin.site.register(Course)
admin.site.register(Course_picture)
