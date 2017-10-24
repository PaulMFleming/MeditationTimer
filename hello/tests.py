# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from hello.views import get_index, get_guide
from django.core.urlresolvers import resolve
# Create your tests here.

class HomeTestPage(TestCase):
    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

class GuideTestPage(TestCase):
    def test_guide_page_resolves(self):
        guide_page = resolve('/guide/')
        self.assertEqual(guide_page.func, get_guide)