from django.shortcuts import render

from models import Device
from serializers import DeviceSerializer

from rest_framework.viewsets import ModelViewSet

# Create your views here.

class DeviceViewSet(ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()