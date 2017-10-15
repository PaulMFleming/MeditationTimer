# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_index(request):
    return render(request, 'index.html')

def get_guide(request):
    return render(request, 'guide.html')
