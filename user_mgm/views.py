from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User, Group

from models import UserProfile
from serializers import UserProfileSerializer, UserSerializer, GroupSerializer, CreateUserSerializer

from company_mgm.models import Company

import djoser.views

# Create your views here.


#API VIEWS

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])

        serializer = UserSerializer(user, request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            company = get_object_or_404(Company, pk=request.data['company'])
            for group in request.data['groups']:
                gr = get_object_or_404(Group, pk=group)

            user = User.objects.create_user(username=request.data['username'], password=request.data['password'])
            for group in request.data['groups']:
                user.groups.add(gr)

            user.save()
            profile = UserProfile(user=user, company=company)
            profile.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer