from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from company_mgm.models import Company

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')
    #TODO add needed fields
    company = models.ForeignKey(Company, default=None, blank=True, null=True)