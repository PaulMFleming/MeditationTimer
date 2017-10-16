# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.

class UploadImage(models.Model):
    """
    Define how the user will upload images
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL) # link author to the registered user
    myimage = models.ImageField(upload_to='myimages/')
    uploaded_at = models.DateTimeField(auto_now_add=True)