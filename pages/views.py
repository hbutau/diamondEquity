# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render
from django.views.generic import TemplateView

from .models import About, PropertyListing

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, ** kwargs):
        context = super(HomeView, self).get_context_data( ** kwargs)
        context['about_us'] = About.objects.all()
        context['featured_properties'] = PropertyListing.objects.all()
        return context
