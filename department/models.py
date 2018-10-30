# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# inherit timezone
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

# import reverse
from django.urls import reverse

class Department(models.Model):
    department_name=models.CharField(max_length=300, unique=True)
    department_floor=models.IntegerField()
    department_head=models.ForeignKey(User)
    date_created=models.DateTimeField(default=timezone.now)
    assignee = models.ForeignKey(User, null=True, related_name='assignee')
    

    def __str__(self):
        return self.department_name
    
    def get_absolute_url(self):
        return reverse('all-departments')
