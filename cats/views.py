from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Cat

def all_cats(request):
    """ a view to show all of the cats, including sorting and search queries """

    cats = Cat.objects.all()
    query = None
    sort_by_gender = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('cats'))

            queries = Q(name__icontains=query) | Q(breed__icontains=query) | Q(colour__icontains=query) | Q(gender__icontains=query)
            cats = cats.filter(queries)

    sortkey = request.GET.get('sortkey', 'name')

    if sortkey == 'cat':
        sortkey = 'cat__name'

    if 'direction' in request.GET and request.GET['direction'] == 'desc':
        sortkey = f'-{sortkey}'
    
    cats = cats.order_by(sortkey)

    if 'sort' in request.GET:
        sort_by_gender = request.GET['sort']
        if sort_by_gender == 'male':
            cats = cats.filter(gender='M')
        elif sort_by_gender == 'female':
            cats = cats.filter(gender='F')

    # get unique breeds and colours for filtering options, breeds and colours
    ## that appear multiple times in database are only shown once
    unique_breeds = Cat.objects.order_by('breed').values_list('breed', flat=True).distinct()
    unique_colour = Cat.objects.order_by('colour').values_list('colour', flat=True).distinct()

    context = {
        'cats': cats,
        'search_term': query,
        'sort_by_gender': sort_by_gender,
        'unique_breeds': unique_breeds,
        'unique_colour': unique_colour,
    }

    return render(request, 'cats/cats.html', context)


def cats_by_breed(request, breed):
    """ A view to show all cats of a specific breed """
    cats = Cat.objects.filter(breed=breed)

    context = {
        'cats': cats,
        'breed': breed,
    }

    return render(request, 'cats/cats.html', context)


def cats_by_colour(request, colour):
    """ A view to show all cats of a specific colour """
    cats = Cat.objects.filter(colour=colour)

    context = {
        'cats': cats,
        'colour': colour,
    }

    return render(request, 'cats/cats.html', context)


def cat_detail(request, cat_id):
    """ a view to show individual cat record """

    cat = get_object_or_404(Cat, pk=cat_id)

    context = {
        'cat': cat,
    }

    return render(request, 'cats/cat_detail.html', context)