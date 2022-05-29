from unicodedata import name
from django.test import TestCase
from .models import *



# TestCases for the Location Model
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

    def test_update_location(self):
        self.new_location.save()
        self.new_location.update(self.new_location.id, "maldives")
        update = Location.objects.get(name = "maldives")
        self.assertTrue(update.name == 'maldives')

    def tearDown(self):
        Location.objects.all().delete()



# TestCases for the Category Model
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

    def test_update_location(self):
        self.new_category.save()
        self.new_category.update(self.new_category.id, "fun")
        update = Category.objects.get(name = "fun")
        self.assertTrue(update.name == 'fun')

    def tearDown(self):
        Image.objects.all().delete()



# TestCases for the Image Model
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

    def test_delete_image(self):
        self.new_image.save()
        self.new_image.delete()
        self.assertTrue(len( Image.objects.all()) == 0)

    def test_update_Image(self):
        location = Location(name='Maldives')
        location.save()
        category = Category(name='Vacation')
        category.save()
        self.new_image.save()
        self.new_image.update(self.new_image.id, "updated-name", 'updated-description', category.id, location.id)
        update = Image.objects.get(
            name = "updated-name",
            description = 'updated-description',
            category = category.id,
            location = location.id
            )
        self.assertTrue(update.name == 'updated-name')

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