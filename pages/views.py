# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponseRedirect

from .models import About, PropertyListing, Contact
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'index.html'


    contact_form = ContactForm()
    def get_context_data(self, ** kwargs):
        context = super(HomeView, self).get_context_data( ** kwargs)
        contact_form = ContactForm()
        context['about_us'] = About.objects.all()
        context['featured_properties'] = PropertyListing.objects.all()
        context['contact_form'] = contact_form
        return context


def contact(request):
    # check captcha
    if request.method == "POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            # process the data in contact_form.cleaned_data as required
            obj = Contact()  # gets new object
            obj.name = contact_form.cleaned_data['name']
            obj.company = contact_form.cleaned_data['company']
            obj.email = contact_form.cleaned_data['email']
            obj.message = contact_form.cleaned_data['message']
            # finally save the object in db
            obj.save()

            # send email to pycon_zim@gmail.com
            subject = "Message on Contact Form "
            message = 'A message was submitted on the website\n\n'
            message += 'Name: ' + contact_form.cleaned_data['name'] + '\n'
            message += 'Email: ' + contact_form.cleaned_data['email'] + '\n'
            message += 'Company: ' + contact_form.cleaned_data['company'] + '\n'
            message += 'Message:\n ' + contact_form.cleaned_data['message'] + '\n'

            sender = 'diamond@gmail.com'

            recipient_list = ['diamond@gmail.com']
            send_mail(subject, message, sender, recipient_list)

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('pages:index'))

    else:
        # if a GET (or any other method) we'll create a blank form
        contact_form = ContactForm()

        return HttpResponseRedirect(reverse('pages:index'))

