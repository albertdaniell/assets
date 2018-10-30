# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# inherit timezone
from django.utils import timezone

# import user model

from django.contrib.auth.models import User
# Import department model
from department.models import Department
# import assetname model
from assetname.models import Assetname
# import reverse
from django.urls import reverse

# Create your models here.

class AssetManager(models.Model):
    asset_serial_number=models.IntegerField(unique=True)
    asset_name=models.ForeignKey(Assetname ,on_delete=models.CASCADE)
    asset_brand=models.CharField(max_length=300)
    asset_specification=models.TextField()
    department_assigned = models.ForeignKey(Department)
    date_added=models.DateTimeField(default=timezone.now)
    assignee = models.ForeignKey(User ,on_delete=models.CASCADE)

    def __str__(self):
        return self.asset_brand

    def get_absolute_url(self):
        return reverse('asset-index')
    


