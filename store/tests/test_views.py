from unittest import skip
from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product
from django.urls import reverse

from django.test import Client

# coverage run --omit='*/venv/*' manage.py test - use for test

# @skip('example skip')
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass
    

class TestViewsResponses(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        Category.objects.create(name='Django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price=20.00, image='django')
        
    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)
        
    def test_category_detail_url(self):
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)
        