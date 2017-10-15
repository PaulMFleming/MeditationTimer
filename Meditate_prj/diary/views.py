# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import DiaryEntryForm
from .models import DiaryEntry

# Create your views here.

# this view is a test & isn't working yet

def entry_list(request):
    """
    Return all the diary entries owner by logged in user and 
    render them to the diaryentries.html template
    """
    entries = DiaryEntry.objects.filter(author=request.user)
    context = {'entries': entries}
    return render(request, "diaryentries.html", context)

def entry_detail(request, id):
    """
    Return a single diary entry based on
    the entry ID and render it to the 
    entrydetail.html template. Or return
    a 404 error
    """
    entry = get_object_or_404(DiaryEntry, pk=id)
    context = {'entry': entry}
    return render(request, "entrydetail.html", context)

def new_entry(request):
    if request.method == "POST":
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.created_date = timezone.now()
            entry.save()
            return redirect(entry_detail, entry.pk)
    else:
        form = DiaryEntryForm()
        context = {'form': form}
        return render(request, 'diaryentryform.html', context)
