# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class DiaryEntry(models.Model):
    """
    Define the diary entry model here
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL) # link author to the registered user
    title = models.CharField(max_length=200) # set this to be the date later on
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    intention = models.TextField()

    def publish(self):
        self.save()

    def __unicode__(self):
        return self.title
