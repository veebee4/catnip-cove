from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Cat(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    age = models.IntegerField
    breed = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name