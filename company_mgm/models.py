from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    company = models.ForeignKey(Company, related_name='locations', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



