from django.db import models


class Location(models.Model):
    """
    Model representing a location.

    Attributes:
        name (str): The name of the location.

    Methods:
        save(self, *args, **kw): Overrides the save method to add custom behavior.
        delete(self, *args, **kw): Overrides the delete method to add custom behavior.
        __str__(self): Returns a string representation of the location.
        update(cls, id, value): Updates the name of the location with the specified ID.

    """

    name = models.CharField(max_length=100)

    def save(self, *args, **kw):
        super(Location, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Location, Location.objects.get(id=self.id)).delete(*args, **kw)

    def __str__(self):
        return self.name

    @classmethod
    def update(cls, id, value):
        cls.objects.filter(id=id).update(name=value)


class Category(models.Model):
    """
    Model representing a category.

    Attributes:
        name (str): The name of the category.

    Methods:
        save(self, *args, **kw): Overrides the save method to add custom behavior.
        delete(self, *args, **kw): Overrides the delete method to add custom behavior.
        __str__(self): Returns a string representation of the category.
        update(cls, id, value): Updates the name of the category with the specified ID.

    """

    name = models.CharField(max_length=100)

    def save(self, *args, **kw):
        super(Category, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Category, Category.objects.get(id=self.id)).delete(*args, **kw)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

    @classmethod
    def update(cls, id, value):
        cls.objects.filter(id=id).update(name=value)


class Image(models.Model):
    """
    Model representing an image.

    Attributes:
        image (ImageField): The uploaded image file.
        name (str): The name of the image.
        description (str): The description of the image.
        location (ForeignKey): The associated location.
        category (ForeignKey): The associated category.

    Methods:
        save(self, *args, **kw): Overrides the save method to add custom behavior.
        delete(self, *args, **kw): Overrides the delete method to add custom behavior.
        __str__(self): Returns a string representation of the image.
        update(cls, id, name, description, category, location): Updates the image with the specified ID and attributes.
        get_image_by_id(cls, id): Retrieves the image with the specified ID.
        search_by_category(cls, category): Searches for images based on the specified category.
        filter_by_location(cls, location): Filters images based on the specified location.

    """

    image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kw):
        super(Image, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Image, Image.objects.get(id=self.id)).delete(*args, **kw)

    def __str__(self):
        return self.name

    @classmethod
    def update(cls, id, name, description, category, location):
        cls.objects.filter(id=id).update(
            name=name,
            description=description,
            category=category,
            location=location
        )

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.get(id=id)
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category=category.id)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.get(location=location)
        return images
