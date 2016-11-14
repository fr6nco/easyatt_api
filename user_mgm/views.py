from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User, Group

from models import UserProfile
from serializers import UserProfileSerializer, UserSerializer, GroupSerializer

# Create your views here.


#API VIEWS

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer