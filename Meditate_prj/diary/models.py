# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings
from django import forms

# Create your models here.

BODY_CHOICES = [
    ('restless or jittery', 'restless or jittery'),
    ('lots of sensations and let them pass by', 'lots of sensations and let them pass by'),
    ('loose and calm', 'loose and calm'),
    ('like it was floating away', 'like it was floating away'),
    ('like it blended into everything around me', 'like it blended into everything around me'),
]

MIND_CHOICES = [
    ('wandered a lot', 'wandered a lot'),
    ('let lots of thoughts pass me by', 'let lot of thoughts pass me by'),
    ('was at peace and felt calm', 'was at peace and felt calm'),
    ('hung out in the gaps between my thoughts', 'hung out in the gaps between my thoughts'),
    ('blended into everything around me', 'blended into everything around me'),
]

class DiaryEntry(models.Model):
    """
    Define the diary entry model here
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL) # link author to the registered user
    title = models.CharField(max_length=200) # set this to be the date later on
    created_date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=200, choices=BODY_CHOICES, null=True, default='OK')
    mind = models.CharField(max_length=200, choices=MIND_CHOICES, null=True, default='OK')
    insights = models.TextField()

    def publish(self):
        self.save()

    def __unicode__(self):
        return self.title
