from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Cat

def all_cats(request):
    """ a view to show all of the cats, including sorting and search queries """

    cats = Cat.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse,('cats'))

            queries = Q(name__icontains=query) | Q(breed__icontains=query) | Q(colour__icontains=query) | Q(gender__icontains=query)
            cats = cats.filter(queries)


    context = {
        'cats': cats,
        'search_term': query,
    }

    return render(request, 'cats/cats.html', context)


def cat_detail(request, cat_id):
    """ a view to show individual cat record """

    cat = get_object_or_404(Cat, pk=cat_id)

    context = {
        'cat': cat,
    }

    return render(request, 'cats/cat_detail.html', context)