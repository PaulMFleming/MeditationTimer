# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ImageForm, AudioForm
from .models import UploadImage
# Create your views here.

def ImageCreate(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = { "form": form }
    return render(request, "myimages.html", context)

def AudioCreate(request):
    form = AudioForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = { "form": form }
    return render(request, "mysounds.html", context)