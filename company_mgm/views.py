from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from models import Location, Company
from serializers import LocationSerializer, CompanySerializer, LocationDetailSerializer, CompanyDetailSerializer
# Create your views here.


#API VIEWS

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def retrieve(self, request, *args, **kwargs):
        location = Location.objects.get(pk=kwargs['pk'])
        serializer = LocationDetailSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def retrieve(self, request, *args, **kwargs):
        company = Company.objects.get(pk=kwargs['pk'])
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)


