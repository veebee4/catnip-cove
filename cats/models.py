from django.db import models


GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]


class Cat(models.Model):
    name = models.CharField(max_length=50)
    age_if_known = models.CharField(max_length=10)
    breed = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
