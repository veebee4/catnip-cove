from django.contrib import admin
from .models import Cat

class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_if_known', 'breed', 'colour', 'gender', 'description', 'image_url', 'image')

admin.site.register(Cat, CatAdmin)
