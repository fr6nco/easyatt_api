from rest_framework import serializers
from models import RFid
from django.contrib.auth.models import User

class RFidSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = RFid
        fields = ('id', 'rfid', 'token_type', 'token_status', 'user')

class RFidCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, allow_null=True)
    class Meta:
        model = RFid
        fields = ('id', 'rfid', 'token_type', 'token_status', 'user')