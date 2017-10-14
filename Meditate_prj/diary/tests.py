# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone
from .models import DiaryEntry
import datetime

# Create your tests here.

class DiaryEntryTests(TestCase):
    """
    Define the tests to run against
    the DiaryEntry model
    """

    def test_title(self):
        test_title = DiaryEntry(title=datetime.datetime.now())
        self.assertEqual(test_title, datetime.datetime.now())