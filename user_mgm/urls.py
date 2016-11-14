__author__ = 'thomas'
from rest_framework import routers
from views import UserViewSet, GroupViewSet

user_mgm_router = routers.SimpleRouter()
user_mgm_router.register(r'users', UserViewSet)
user_mgm_router.register(r'groups', GroupViewSet)

def getUrlPatterns():
    return user_mgm_router.urls