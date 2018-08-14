from django.contrib import admin
from .models import User, Manager, Operating_history
# Register your models here.
admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Operating_history)