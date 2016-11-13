__author__ = 'thomas'
from rest_framework import routers
from views import RFidViewSet

card_mgm_router = routers.SimpleRouter()
card_mgm_router.register(r'rfids', RFidViewSet)

def getUrlPatterns():
    return card_mgm_router.urls