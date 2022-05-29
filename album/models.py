from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kw):
        super(Location, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Location, Location.objects.get(id=self.id)).delete(*args, **kw)

    # def update(self, property, value):
    #     super(Location, Location.objects.get(name = self.name)).save(update_fields=[property ])

    def __str__(self):
        return self.name

    



class Category(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kw):
        super(Category, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Category, Category.objects.get(id=self.id)).delete(*args, **kw)

    # def update(self, attribute, value):
    #     Category.objects.get(id=self.id).update(attribute = value)

    def __str__(self):
        return self.name






class Image(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kw):
        super(Image, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Image, Image.objects.get(id=self.id)).delete(*args, **kw)

    # def update(self, attribute, value):
    #     Image.objects.get(id=self.id).update(attribute = value)

    def __str__(self):
        return self.name

    
    # @classmethod
    # def get_image_by_id(id):
    #     image = Image.objects.get(id=id).first()
    #     return image

    # @classmethod
    # def search_by_category(category):
    #     images = Image.objects.get(category=category).all()
    #     return images

    # @classmethod
    # def filter_by_location(location):
    #     images = Image.objects.get(location=location).all()
    #     return images

        

    


