# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from useruploads.views import ImageCreate
from django.core.urlresolvers import resolve

# Create your tests here.

class UploadImagePageTest(TestCase):
    def test_upload_image_page_resolves(self):
        upload_image_page = resolve('/myimages/')
        self.assertEqual(upload_image_page.func, ImageCreate)

    def test_upload_image_page_status_code_is_ok(self):
        upload_image_page = self.client.get('/myimages/')
        self.assertEqual(upload_image_page.status_code, 200)
