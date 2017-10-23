# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

class SimpleTest(TestCase):
    def test_adding_something_simple(self):
        self.assertEqual( 1+2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual( 1+2, 4)