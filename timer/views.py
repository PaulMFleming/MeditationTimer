# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from useruploads.models import UploadImage

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_timer(request):
    return render(request, 'timer.html')

def get_mytimer(request):
    return render(request, 'mytimer.html')

def get_myimages(request):
    myimages = UploadImage.objects.filter(author=request.user)
    context = {'myimages': myimages}
    return render(request, "mytimer.html", context)