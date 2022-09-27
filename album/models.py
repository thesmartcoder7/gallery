from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kw):
        super(Location, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Location, Location.objects.get(id=self.id)).delete(*args, **kw)

    def __str__(self):
        return self.name


    @classmethod
    def update(cls, id, value):
        cls.objects.filter(id = id).update(name = value)

    



class Category(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kw):
        super(Category, self).save(*args, **kw)

    def delete(self, *args, **kw):
        super(Category, Category.objects.get(id=self.id)).delete(*args, **kw)

    def __str__(self):
        return self.name


    @classmethod
    def update(cls, id, value):
        cls.objects.filter(id = id).update(name = value)





class Image(models.Model):
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
            name = name,
            description = description,
            category = category,
            location = location
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

        

    


