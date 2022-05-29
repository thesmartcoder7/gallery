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
    #     self.new_location.save()
    #     self.new_location.update(self.new_location.name,"Maldives")
    #     self.assertTrue(self.new_location.name ==  "Maldives")

    def tearDown(self):
        Location.objects.all().delete()




# class ImageModelTest(TestCase):
#     def setUp(self):
#         location = Location(name='Maldives')
#         category = Category(name='Vacation')
#         self.new_image = Image(name='family in maldives', category=category, location=location, description='this was the time my family and I went to maldives for the holidays')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.new_image, Image))

#     def test_image_save(self):
#         self.new_image.save()
#         self.assertTrue(len( Image.objects.all()) == 1)

#     def tearDown(self):
#         Image.objects.all().delete()