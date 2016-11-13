from django.shortcuts import render, get_object_or_404

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
        #TODO token assignation validation
        serializer = RFidCreateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        rfid = get_object_or_404(RFid, pk=kwargs['pk'])
        print request.data
        if 'user' in request.data and request.data['user'] is not None:
            rfid.token_status = RFid.TOKEN_ASSIGNED

        if 'user' in request.data and request.data['user'] is None:
            rfid.token_status = RFid.TOKEN_UNASSIGNED

        if 'token_status' in request.data and (request.data['token_status'] == RFid.TOKEN_UNASSIGNED or request.data['token_status'] == RFid.TOKEN_LOST):
            rfid.user = None

        serializer = RFidCreateSerializer(rfid, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)