from unittest import skip

# from django.test import TestCase
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase  # advance tests
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products

# coverage run --omit='*/venv/*' manage.py test - use for test

# @skip('example skip')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
    

class TestViewsResponses(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='Django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price=20.00, image='django')
        
    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        
    # def test_url_allowed_hosts(self):
    #     response = self.c.get('/', HTTP_HOST='noadress.com')
    #     self.assertEqual(response.status_code, 400)
    #     response = self.c.get('/', HTTP_HOST='yourdomain.com')
    #     self.assertEqual(response.status_code, 200)  after add in ALLOWED_HOSTS = []
        
    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)
        
    def test_category_detail_url(self):
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)
        
    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_function(self):
        request = self.factory.get('item/django-beginners')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)