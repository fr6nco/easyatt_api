from __future__ import unicode_literals

from django.db import models

from company_mgm.models import Location

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, default=None, null=True)
    location = models.ForeignKey(Location, related_name='device')
    api_key = models.CharField(max_length=1024)

    class Meta:
        permissions = (
            ('open_door', 'Open door'),
        )

    is_authenticated = True