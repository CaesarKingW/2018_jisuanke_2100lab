from rest_framework import serializers
from .models import User, Message, Course, Order, Course_picture


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

    class Meta:
        model = Message
        fields = ('id', 'user_phone', 'course_title', 'course_id', 'content',
                  'created_at', 'praise_count')

    def get_course_title(self, obj):
        return obj.course_id.title


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('Order_number', 'user_phone', 'course_id', 'amount_of_money',
                  'status', 'create_at')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'brief_introduction', 'audio', 'whole_introduction',
                  'Is_distory', 'distory_time', 'Is_free', 'price',
                  'share_rate', 'can_comment')



class Course_pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_picture
        fields = ('course_id', 'course_picture', 'start_time', 'end_time')
