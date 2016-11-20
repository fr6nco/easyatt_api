from rest_framework import serializers
import json

from models import UserProfile
from django.contrib.auth.models import User, Group

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    company = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    groups = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    company = serializers.IntegerField()
    class Meta:
        model = User
        fields = ('id', 'username', 'company', 'password', 'groups')