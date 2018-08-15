# head_protrait = models.ImageField(
#     upload_to=None,
#     height_field=None,
#     width_field=None,
#     max_length=None)
from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=11, primary_key=True)
    username = models.CharField(blank=True, null=True, max_length=15)
    head_protrait = models.ImageField(
        upload_to='user_photos/', blank=True, null=True)
    welfare = models.FloatField(default=0.0)
    Can_comment = models.BooleanField(default=True)
    Is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number


class Manager(models.Model):
    username = models.CharField(null=False, max_length=15, primary_key=True)
    password = models.CharField(null=False, max_length=50)
    Supermanager = models.BooleanField(default=False)
    Manage_course = models.BooleanField(default=False)
    Manage_user = models.BooleanField(default=False)
    Manage_message = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Operating_history(models.Model):
    manager_username = models.ForeignKey('Manager', on_delete=models.CASCADE)
    operate_type = models.CharField('操作类型', max_length=50)
    object_type = models.CharField('操作对象', max_length=50)
    created_at = models.DateTimeField(
        default=timezone.now, auto_now=False, auto_now_add=False)


class Course(models.Model):
    title = models.CharField('标题', max_length=50)
    brief_introduction = models.TextField('简介')
    audio = models.FileField(("音频"), upload_to='audio/', blank=True, null=True)
    whole_introduction = models.FileField(
        ("详解"), upload_to='word/', blank=True, null=True)
    Is_distory = models.BooleanField(("是否阅后即焚"), default=False)
    distory_time = models.DurationField(("可阅时长"), blank=True, null=True)
    Is_free = models.BooleanField(("免费"), default=True)
    price = models.FloatField(("价格"), blank=True, null=True, default=0.0)
    sale_count = models.PositiveIntegerField(
        ("销量"), blank=True, null=True, default=0)
    view_count = models.PositiveIntegerField(("观看量"), default=0)
    share_rate = models.FloatField(("分销比例"), blank=True, null=True)
    can_comment = models.BooleanField(("允许用户留言"), default=True)

    def __str__(self):
        return str(self.id)


class Course_picture(models.Model):
    course_id = models.ForeignKey("Course", on_delete=models.CASCADE)
    course_picture = models.ImageField(
        ("课程图片"), upload_to='course_picture', blank=True, null=True)
    start_time = models.DurationField((""))
    end_time = models.DurationField((""))


class Takes(models.Model):
    user_phone = models.ForeignKey("User", on_delete=models.CASCADE)
    course_id = models.ForeignKey("Course", on_delete=models.CASCADE)
    start_time = models.DateTimeField(("开始学习时间"), auto_now_add=True)


class Order(models.Model):
    Order_number = models.CharField(("订单号"), max_length=30, primary_key=True)
    user_phone = models.ForeignKey("User", on_delete=models.CASCADE)
    course_id = models.ForeignKey("Course", on_delete=models.CASCADE)
    course_price = models.FloatField(("价格"))
    status = models.CharField('订单状态', max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user_name = models.ForeignKey(
        "User", verbose_name=("用户号码"), on_delete=models.CASCADE)
    course_id = models.ForeignKey(
        "Course", verbose_name=("课程编号"), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    praise_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Reply(models.Model):
    message_id = models.ForeignKey(
        "Message", verbose_name=("留言编号"), on_delete=models.CASCADE)
    user_phone = models.ForeignKey(
        "User", verbose_name=("用户号码"), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
