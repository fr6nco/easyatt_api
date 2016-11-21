from __future__ import unicode_literals

from django.db import models

from device_mgm.models import Device
from django.contrib.auth.models import User


class AttendanceEntry(models.Model):
    WORK_IN = 'work_in'
    WORK_OUT = 'work_out'
    HOLIDAY_IN = 'holiday_in'
    HOLIDAY_OUT = 'holiday_out'
    BREAK_IN = 'break_in'
    BREAK_OUT = 'break_out'
    ACCESS = 'access'

    ENTRY_TYPES = (
        (WORK_IN, 'Work in'),
        (WORK_OUT, 'Work out'),
        (HOLIDAY_IN, 'Holiday in'),
        (HOLIDAY_OUT, 'Holiday out'),
        (BREAK_IN, 'Break in'),
        (BREAK_OUT, 'Break out'),
        (ACCESS, 'Access')
    )

    ACCESS_DENIED = 'access_denied'
    ACCESS_GRANTED = 'access_granted'

    RESULT_TYPES = (
        (ACCESS_DENIED, 'Access Denied'),
        (ACCESS_GRANTED, 'Access Granted'),
    )

    device = models.ForeignKey(Device, related_name='attendance_entries')
    user = models.ForeignKey(User, related_name='attendance_entries')
    entry_type = models.CharField(max_length=25, choices=ENTRY_TYPES, default=ACCESS)
    timestamp = models.DateTimeField(auto_now_add=True)
    access_result = models.CharField(max_length=25, choices=RESULT_TYPES, default=None, null=True, blank=True)

    def __str__(self):
        return '%s at %s on device %s' % (self.entry_type, self.timestamp, self.device)

    class Meta:
        verbose_name_plural = 'Attendance entries'

