__author__ = 'thomas'
from rest_framework import routers
from views import LocationViewSet, CompanyViewSet

company_mgm_router = routers.SimpleRouter()
company_mgm_router.register(r'locations', LocationViewSet)
company_mgm_router.register(r'companies', CompanyViewSet)

def getUrlPatterns():
    return company_mgm_router.urls