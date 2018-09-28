from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    class Meta:
        ordering = ['name']

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images/', default=True)
    name = models.CharField(max_length=30)
    description = HTMLField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    category=models.ManyToManyField(Category)
    # pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def search_by_name(cls,search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images

    @classmethod
    def search_by_description(cls,search_term):
        images = cls.objects.filter(description__icontains=search_term)
        return images

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images




