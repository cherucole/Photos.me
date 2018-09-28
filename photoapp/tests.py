from django.test import TestCase
from .models import *
#instead of importing items/classes one by one use * to import everything
from .models import *
import datetime as dt

class TestImage(TestCase):
    def setUp(self):
        self.drinks=Image


#  test Location class
class TestLocation (TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Location))


class TestCategories (TestCase):
    def setUp(self):
        self.nature = Category(name='beach')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))
































