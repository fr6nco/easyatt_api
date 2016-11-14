from rest_framework import serializers

from models import UserProfile
from django.contrib.auth.models import User, Group

class UserProfileSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()
    class Meta:
        model = UserProfile
        fields = ('id', 'company')

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

