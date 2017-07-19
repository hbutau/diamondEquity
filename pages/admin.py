# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib import admin

from .models import PropertyListing

class PropertyListingModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'cost', 'status', 'timestamp']
    class Meta:
        model = PropertyListing
admin.site.register(PropertyListing, PropertyListingModelAdmin)
