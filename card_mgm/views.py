from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from serializers import RFidSerializer, RFidCreateSerializer
from models import RFid

class RFidViewSet(ModelViewSet):
    serializer_class = RFidSerializer
    queryset = RFid.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = RFidCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)