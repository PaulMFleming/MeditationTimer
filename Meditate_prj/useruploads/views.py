# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import ImageForm, AudioForm
from .models import UploadImage
# Create your views here.

def ImageCreate(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.save()
            return redirect('mytimer')
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