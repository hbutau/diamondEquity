# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from PIL import Image
import sys, time

STATUS_CHOICES = (
    ('On Rent', 'On Rent'),
    ('For Sale', 'For Sale'),
)

class PropertyListing(models.Model):
    name = models.CharField(_("Title"), max_length=255, null=True, blank=True)
    # image = models.ImageField()
    cost = models.CharField(_("Costing"), max_length=255, null=True, blank=True)
    status = models.CharField(_("Status"), max_length=255, null=True, blank=True, choices=STATUS_CHOICES)
    location = models.CharField(_("Location"), max_length=255, null=True, blank=True)
    description = models.TextField(_("Description"))
    timestamp = models.DateTimeField(auto_now_add=True)
    """
    three size sets:
        thumbnail (photo_thumb)
        medium (photo_medium)
        original (photo_original)
    """

    now = str(int(time.time()))
    filepath = 'media/'+now+'/'

    photo_original = models.FileField('original file upload', upload_to=filepath)
    photo_medium = models.CharField(max_length=255, blank=True)
    photo_thumb = models.CharField(max_length=255, blank=True)
    photo_credits = models.CharField(max_length=255, blank=True)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_thumb(self):
        return "/media/%s" % self.photo_thumb

    def get_medium(self):
        return "/media/%s" % self.photo_medium

    def get_original(self):
        return "/media/%s" % self.photo_original

    def save(self):
        sizes = {'thumbnail': {'height': 100, 'width': 100}, 'medium': {'height': 300, 'width': 300},}

        super(PropertyListing, self).save()
        photopath = str(self.photo_original.path)  # this returns the full system path to the original file
        im = Image.open(photopath)  # open the image using PIL

	# pull a few variables out of that full path
        extension = photopath.rsplit('.', 1)[1]  # the file extension
        filename = photopath.rsplit('/', 1)[1].rsplit('.', 1)[0]  # the file name only (minus path or extension)
        fullpath = photopath.rsplit('/', 1)[0]  # the path only (minus the filename.extension)

        # use the file extension to determine if the image is valid before proceeding
        if extension not in ['jpg', 'jpeg', 'gif', 'png']: sys.exit()

        # create medium image
        im.thumbnail((sizes['medium']['width'], sizes['medium']['height']), Image.ANTIALIAS)
        medname = filename + "_" + str(sizes['medium']['width']) + "x" + str(sizes['medium']['height']) + ".jpg"
        im.save(fullpath + '/' + medname)
        self.photo_medium = self.filepath + medname

        # create thumbnail
        im.thumbnail((sizes['thumbnail']['width'], sizes['thumbnail']['height']), Image.ANTIALIAS)
        thumbname = filename + "_" + str(sizes['thumbnail']['width']) + "x" + str(sizes['thumbnail']['height']) + ".jpg"
        im.save(fullpath + '/' + thumbname)
        self.photo_thumb = self.filepath + thumbname

        super(PropertyListing, self).save()

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Property Listing"
        verbose_name_plural = "Property Listings"


class About(models.Model):
    title = models.TextField()
    sub_heading = models.TextField()
    paragraph_text = models.TextField()


class Contact(models.Model):
    name = models.CharField("full name", max_length=120)
    company = models.CharField("company name", max_length=120)
    email = models.EmailField("email address", max_length=120)
    message = models.TextField()
    # email_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

