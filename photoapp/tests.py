from django.test import TestCase
from .models import *
#instead of importing items/classes one by one use * to import everything
class TestImage(TestCase):
    # def class instance setup for the project
    def setUp(self):
        self.diani = Location.objects.create(name='Diani')
        self.sports = Category.objects.create(name='sports')
        self.logos = Category.objects.create(name='logos')

        self.office = Image.objects.create(
            name='office', location=self.diani,  description='an office picture')

        self.office.categories.add(self.sports)
        self.office.categories.add(self.logos)

    # def a testcase for instance of the office class
    def test_instance(self):
        self.office.save()
        self.assertTrue(isinstance(self.office, Image))

    def test_delete_image(self):
        self.office.save()
        self.office.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.office.save()
        self.office.name = 'update_office'
        self.assertTrue(self.office.name == 'update_office')

    def test_all_images(self):
        self.office.save()
        images = Image.all_images()
        self.assertTrue(len(images) > 0)

    def test_show_by_category(self):
        self.drinks.save()
        images = Image.show_by_category('sports')
        self.assertTrue(len(images) > 0)

    def test_view_location(self):
        self.drinks.save()
        location = Image.show_by_location(self.nairobi)
        self.assertTrue(len(location) > 0)

class TestCategories (TestCase):
    def setUp(self):
        self.nature = Category(name='beach')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))

#  test Location class
class TestLocation (TestCase):
    def setUp(self):
        self.nairobi = Location(name='Nairobi')

    def test_instance(self):
        self.nairobi.save()
        self.assertTrue(isinstance(self.nairobi, Location))












