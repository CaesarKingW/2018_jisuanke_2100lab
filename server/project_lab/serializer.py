from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('phone_number', 'user_name', 'head_protrait', 'welfare', 'Can_comment', 'Is_teacher')
