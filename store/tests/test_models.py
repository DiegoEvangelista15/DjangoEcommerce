from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product

class TestCategoriesModels(TestCase):
    
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='Django', slug='django')
        
    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        
    def test_category_model_entry(self):
        data = self.data1
        self.assertEqual(str(data), 'Django')
        
class TestProductsModels(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='Django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1, slug='django-beginners', price=20.00, image='django')
        
    def test_product_models_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')