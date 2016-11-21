__author__ = 'thomas'
from rest_framework import routers
from views import AttendanceEntryViewSet

att_mgm_router = routers.SimpleRouter()
att_mgm_router.register(r'attendanceentries', AttendanceEntryViewSet)

def getUrlPatterns():
    return att_mgm_router.urls