from rest_framework import serializers
from .models import User, Message, Course, Order, Course_picture, Manager
from .models import Reply


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'user_name', 'head_protrait', 'welfare',
                  'Can_comment', 'Is_teacher')


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('username', 'Supermanager', 'Manage_course', 'Manage_user',
                  'Manage_message', 'Manage_order')


class MessageSerializer(serializers.ModelSerializer):
    course_title = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('id', 'user_phone', 'course_title', 'user_name', 'course_id',
                  'content', 'created_at', 'praise_count')

    def get_course_title(self, obj):
        return obj.course_id.title

    def get_user_name(self, obj):
        return obj.user_phone.user_name


class ReplySerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = ('id', 'message_id', 'user_phone', 'user_name', 'content',
                  'created_at')

    def get_user_name(self, obj):
        return obj.user_phone.user_name


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('Order_number', 'user_phone', 'course_id', 'amount_of_money',
                  'status', 'create_at')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'brief_introduction', 'audio',
                  'whole_introduction', 'Is_distory', 'distory_time',
                  'Is_free', 'price', 'share_rate', 'can_comment')


class Course_pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_picture
        fields = ('id', 'course_id', 'course_picture', 'start_time',
                  'end_time')
