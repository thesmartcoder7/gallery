from unicodedata import name
from django.test import TestCase
from .models import *

# Create your tests here.
class LocationModelTests(TestCase):
    def setUp(self):
        self.new_location = Location(name='kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_location(self):
        self.new_location.save()
        self.assertTrue(len( Location.objects.all()) == 1)

    def test_delete_location(self):
        self.new_location.save()
        self.new_location.delete()
        self.assertTrue(len( Location.objects.all()) == 0)

    # def test_update_location(self):
    #     self.new_location.update("maldives")
    #     self.assertTrue(self.new_location.name == 'maldives')

    def tearDown(self):
        Location.objects.all().delete()




class CategoryModelTests(TestCase):
    def setUp(self):
        self.new_category = Category(name='Vacation')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    def test_image_save(self):
        self.new_category.save()
        self.assertTrue(len( Category.objects.all()) == 1)

    def test_delete_location(self):
        self.new_category.save()
        self.new_category.delete()
        self.assertTrue(len( Category.objects.all()) == 0)

    # def test_update_location(self):
    #     self.new_category.update("fun")
    #     self.assertTrue(self.new_category.name == 'fun')

    def tearDown(self):
        Image.objects.all().delete()



class ImageModelTests(TestCase):
    def setUp(self):
        location = Location(name='Maldives')
        location.save()
        category = Category(name='Vacation')
        category.save()
        self.new_image = Image(name='family-trip', category=category, location=location, description="this is an image of a family trip to maldives")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_image_save(self):
        self.new_image.save()
        self.assertTrue(len( Image.objects.all()) == 1)

    def test_delete_location(self):
        self.new_image.save()
        self.new_image.delete()
        self.assertTrue(len( Image.objects.all()) == 0)

    def test_get_image_by_id(self):
        self.new_image.save()
        self.assertTrue(Image.get_image_by_id(id=self.new_image.id).name == 'family-trip')

    def test_search_by_category(self):
        self.new_image.save()
        self.assertTrue(len(Image.search_by_category(self.new_image.category)) > 0 )

    def test_filter_by_location(self):
        self.new_image.save()
        self.assertTrue(Image.filter_by_location(self.new_image.location) == self.new_image)

    def tearDown(self):
        Image.objects.all().delete()