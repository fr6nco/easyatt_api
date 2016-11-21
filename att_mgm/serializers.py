from rest_framework import serializers
from models import AttendanceEntry
from django.contrib.auth.models import User

 #
 #    device = models.ForeignKey(Device, related_name='attendance_entries')
 #    user = models.ForeignKey(User, related_name='attendance_entries')
 #    entry_type = models.CharField(max_length=25, choices=ENTRY_TYPES, default=ACCESS)
 #    timestamp = models.DateTimeField(auto_now_add=True)
 #    access_result = models.CharField(max_length=25, choices=RESULT_TYPES, default=None, null=True, blank=True)

class AttendanceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceEntry
        fields = '__all__'


class CreateAttendanceEntrySerializer(serializers.ModelSerializer):
    rfid = serializers.CharField(max_length=255, write_only=True)
    class Meta:
        model = AttendanceEntry
        fields = ('entry_type', 'rfid')
