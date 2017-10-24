# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from timer.views import get_timer, get_mytimer
from django.core.urlresolvers import resolve

# Create your tests here.

class TimerPageTest(TestCase):
    def test_timer_page_resolves(self):
        timer_page = resolve('/timer/')
        self.assertEqual(timer_page.func, get_timer)