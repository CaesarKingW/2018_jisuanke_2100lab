# head_protrait = models.ImageField(
#     upload_to=None,
#     height_field=None,
#     width_field=None,
#     max_length=None)
from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=11)
    username = models.CharField(blank=True, null=True, max_length=15)
    head_protrait = models.ImageField(
        upload_to='user_photos/', blank=True, null=True)
    welfare = models.FloatField(default=0.0)
    Can_comment = models.BooleanField(default=True)
    Is_teacher = models.BooleanField(default=False)

class Manager(models.Model):
    username = models.CharField(null=False, max_length=15)
    password = models.CharField(null=False, max_length=50)
    Supermanager = models.BooleanField(default=False)
    Manage_course = models.BooleanField(default=False)
    Manage_user = models.BooleanField(default=False)
    Manage_message = models.BooleanField(default=False)
    def __str__(self):
         return self.username

class Operating_history(models.Model):
    manager_username=models.ForeignKey('Manager', on_delete=models.CASCADE)
    operate_type=models.CharField('操作类型', max_length=50)
    object_type=models.CharField('操作对象', max_length=50)
    created_at=models.DateTimeField(default=timezone.now, auto_now=False, auto_now_add=False)
