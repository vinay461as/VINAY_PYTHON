from __future__ import unicode_literals

from django.db import models


class Router(models.Model):
    sapid = models.CharField(max_length=50)
    hostname = models.CharField(max_length=50)
    loopback = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
