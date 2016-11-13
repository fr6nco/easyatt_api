from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class RFid(models.Model):

    RFID_CARD = 'card'
    RFID_KEYCHAIN = 'keychain'

    TOKEN_TYPE_CHOICES = (
        (RFID_CARD, 'RFID Card'),
        (RFID_KEYCHAIN, 'RFID Keychain')
    )

    TOKEN_ASSIGNED = 'assigned'
    TOKEN_LOST = 'lost'
    TOKEN_UNASSIGNED = 'unassigned'

    TOKEN_STATUS_CHOICES = (
        (TOKEN_ASSIGNED, 'Assigned'),
        (TOKEN_LOST, 'Lost'),
        (TOKEN_UNASSIGNED, 'Unassigned')
    )

    rfid = models.CharField(max_length=255)
    token_type = models.CharField(choices=TOKEN_TYPE_CHOICES, default=RFID_CARD, max_length=25, null=False)
    token_status = models.CharField(choices=TOKEN_STATUS_CHOICES, default=TOKEN_UNASSIGNED, max_length=25, null=False)
    user = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        verbose_name = 'RFID'
        verbose_name_plural = 'RFIDs'