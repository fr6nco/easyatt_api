from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework.backends import DjangoFilterBackend

from card_mgm.models import RFid


from serializers import AttendanceEntrySerializer, CreateAttendanceEntrySerializer
from models import AttendanceEntry
# Create your views here.

class AttendanceEntryViewSet(ModelViewSet):
    serializer_class = AttendanceEntrySerializer
    queryset = AttendanceEntry.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('user',)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = CreateAttendanceEntrySerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            try:
                rfid = RFid.objects.get(rfid=request.data['rfid'])
            except RFid.DoesNotExist:
                return Response({'Error': 'RFid token not found in DB'}, status=status.HTTP_404_NOT_FOUND)

            user = rfid.user

            device = request.user

            #TODO add restriction so only devices may access this call
            if user.has_perm('can_enter', device.location):
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data={'Error': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

