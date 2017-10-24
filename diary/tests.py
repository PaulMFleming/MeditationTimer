# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from diary.views import entry_list, new_entry
from django.core.urlresolvers import resolve

# Create your tests here.
class NewEntryPageTest(TestCase):
    def test_new_entry_page_resolves(self):
        new_entry_page = resolve('/diary/new/')
        self.assertEqual(new_entry_page.func, new_entry)


class EntryListPageTest(TestCase):
    def test_entry_list_page_resolves(self):
        entry_list_page = resolve('/diaryentries/')
        self.assertEqual(entry_list_page.func, entry_list)

