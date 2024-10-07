from django.shortcuts import render
from .models import Cat

def all_cats(request):
    """ a view to show all of the cats, including sorting and search queries """

    cats = Cat.objects.all()

    context = {
        'cats': cats,
    }

    return render(request, 'cats/cats.html', context)
