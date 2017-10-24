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
        form = ImageForm(request.POST, request.FILES)
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
