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
    username = models.CharField(blank = True, null = True, max_length=15)
    head_protrait = models.ImageField(upload_to='photos/',blank=True,null=True)
    welfare = models.FloatField(default=0.0)
    Can_comment = models.BooleanField(default=True)
    Is_teacher = models.BooleanField(default=False)
