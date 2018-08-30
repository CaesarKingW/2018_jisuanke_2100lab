from rest_framework import serializers
from .models import User, Message, Course, Order, Course_picture, Manager
from .models import Reply, Takes, Operating_history


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'user_name', 'head_protrait', 'welfare',
                  'Can_comment', 'Is_teacher', 'exists')


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
                  'content', 'created_at', 'praise_count','exists')

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
    course_title = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('Order_number', 'user_phone', 'course_id', 'course_title',
                  'amount_of_money', 'status', 'create_at')

    def get_course_title(self, obj):
        return obj.course_id.title


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'brief_introduction', 'audio',
                  'course_duration', 'whole_introduction', 'Cover_picture',
                  'Is_destroy', 'distory_time', 'price', 'share_rate',
                  'can_comment', 'created_at')


class Course_pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_picture
        fields = ('id', 'course_id', 'course_picture', 'start_time',
                  'end_time')


class TakesSerializer(serializers.ModelSerializer):
    course_title = serializers.SerializerMethodField()
    course_duration = serializers.SerializerMethodField()

    class Meta:
        model = Takes
        fields = ('id', 'user_phone', 'course_id', 'course_title',
                  'course_duration', 'start_time', 'last_study_percent',
                  'max_study_percent')

    def get_course_title(self, obj):
        return obj.course_id.title

    def get_course_duration(self, obj):
        return obj.course_id.course_duration


class Operating_historySerializer(serializers.ModelSerializer):
    class Meta:
        model = Operating_history
        fields = ('id', 'manager_username', 'operate_type', 'object_type',
                  'created_at')
