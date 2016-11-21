__author__ = 'thomas'
from rest_framework import routers
from views import DeviceViewSet

device_mgm_router = routers.SimpleRouter()
device_mgm_router.register(r'devices', DeviceViewSet)

def getUrlPatterns():
    return device_mgm_router.urls