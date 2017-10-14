# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .forms import LogForm
from .models import DiaryEntry

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

def entry_list(request):
    entries = DiaryEntry.objects.all()
    context = {'entries': entries}
    return render(request, "diaryentries.html", context)