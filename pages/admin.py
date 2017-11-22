# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib import admin

from .models import PropertyListing
from .models import About

class PropertyListingModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'cost', 'status', 'timestamp']
    list_filter = ('name', 'location', 'status',)
    search_fields = ('name', 'location',)
    class Meta:
        model = PropertyListing
admin.site.register(PropertyListing, PropertyListingModelAdmin)

admin.site.register(About)
