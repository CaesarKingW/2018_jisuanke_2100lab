from rest_framework import serializers
from .models import User, Manager, Course_picture


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


class Course_pictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_picture
        fields = ('course_id', 'course_picture')
