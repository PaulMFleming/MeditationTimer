# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from accounts.views import register, login, logout
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response

# Create your tests here.

class RegisterPageTest(TestCase):
    def test_register_page_resolves(self):
        register_page = resolve('/register/')
        self.assertEqual(register_page.func, register)

    def test_register_page_status_code_is_ok(self):
        register_page = self.client.get('/register/')
        self.assertEqual(register_page.status_code, 200)

    def test_check_content_is_correct(self):
        register_page = self.client.get('/')
        self.assertTemplateUsed(register_page, "index.html")
        register_page_template_output = render_to_response("index.html").content
        self.assertEqual(register_page.content, register_page_template_output)

    

class LoginPageTest(TestCase):
    def test_login_page_resolves(self):
        login_page = resolve('/login/')
        self.assertEqual(login_page.func, login)

    def test_login_page_status_code_is_ok(self):
        login_page = self.client.get('/login/')
        self.assertEqual(login_page.status_code, 200)

    def test_check_content_is_correct(self):
        login_page = self.client.get('/login/')
        self.assertTemplateUsed(login_page, "login.html")

class LogoutPageTest(TestCase):
    def test_logout_page_resolves(self):
        logout_page = resolve('/logout/')
        self.assertEqual(logout_page.func, logout)

    def test_logout_page_status_code_is_ok(self):
        logout_page = self.client.get('/') # logout page redirects to home
        self.assertEqual(logout_page.status_code, 200)

    def test_check_content_is_correct(self):
        logout_page = self.client.get('/') # logout page redirects to home
        self.assertTemplateUsed(logout_page, "index.html")