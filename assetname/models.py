# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# inherit timezone
from django.utils import timezone

# import user model

from django.contrib.auth.models import User
# Import department model
from department.models import Department
# import reverse
from django.urls import reverse

# Create your models here.

class Assetname(models.Model):
    asset_type=models.CharField(max_length=300,unique=True)
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.asset_type
    def get_absolute_url(self):
        return reverse('assetname-index')
