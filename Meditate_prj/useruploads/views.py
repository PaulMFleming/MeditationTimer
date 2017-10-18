# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ImageForm, AudioForm
from .models import UploadImage
# Create your views here.

def ImageCreate(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES['myimage'])
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.save()
            messages.success(request, "Uploaded successfully")
            return redirect('mytimer')
        else:
            messages.error(request, "Unable to upload at this time")
    else:
        form = ImageForm()
    return render(request, "myimages.html", {'form': form})


def AudioCreate(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(form.get_absolute_url())
    else:
        form = AudioForm()
    return render(request, "mysounds.html", {'form': form})


def get_mytimer(request):
    myimages = UploadImage.objects.filter(author=request.user)
    context = {'myimages': myimages}
    return render(request, "mytimer.html", context)