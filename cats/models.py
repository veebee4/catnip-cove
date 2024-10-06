from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField
    breed = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name