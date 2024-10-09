from django.shortcuts import render, get_object_or_404
from .models import Cat

def all_cats(request):
    """ a view to show all of the cats, including sorting and search queries """

    cats = Cat.objects.all()

    context = {
        'cats': cats,
    }

    return render(request, 'cats/cats.html', context)


def cat_detail(request, cat_id):
    """ a view to show individual cat record """

    cat = get_object_or_404(Cat, pk=cat_id)

    context = {
        'cat': cat,
    }

    return render(request, 'cats/cat_detail.html', context)