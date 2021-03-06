"""easyattapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from company_mgm import urls as company_mgm_urls
from card_mgm import urls as card_mgm_urls
from user_mgm import urls as user_mgm_urls
from device_mgm import urls as device_mgm_urls
from att_mgm import urls as att_mgm_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/', include('djoser.urls.authtoken')),
    url(r'^api/v1/', include(company_mgm_urls.getUrlPatterns()), name='company_mgm'),
    url(r'^api/v1/', include(card_mgm_urls.getUrlPatterns()), name='card_mgm'),
    url(r'^api/v1/', include(user_mgm_urls.getUrlPatterns()), name='user_mgm'),
    url(r'^api/v1/', include(device_mgm_urls.getUrlPatterns()), name='device_mgm'),
    url(r'^api/v1/', include(att_mgm_urls.getUrlPatterns()), name='att_mgm'),
]
