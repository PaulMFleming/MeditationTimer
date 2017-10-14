# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LogForm

# Create your views here.

# this view is a test & isn't working yet
def logform(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = LogForm()
    return Http('logform.html', {'form':form},)

