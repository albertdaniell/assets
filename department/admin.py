# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Import models

from .models import Department
# Register your models here so that they show up in admin.

admin.site.register(Department)

