from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Cat
from .forms import CatForm


def all_cats(request):
    """ a view to show all of the cats,
    including sorting and search queries """

    cats = Cat.objects.all()
    query = None
    sort_by_gender = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('cats'))

            queries = (
                Q(name__icontains=query) |
                Q(breed__icontains=query) |
                Q(colour__icontains=query) |
                Q(gender__icontains=query)
            )
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

    """ get unique breeds and colours for filtering options,
    breeds and colours that appear multiple times in database
    are only shown once """
    unique_breeds = Cat.objects.order_by('breed') \
        .values_list('breed', flat=True) \
        .distinct()
    unique_colour = Cat.objects.order_by('colour') \
        .values_list('colour', flat=True) \
        .distinct()

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


@login_required
def add_cat(request):
    """ add a cat to the rescue records """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse, ('home'))

    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES)
        if form.is_valid:
            cat = form.save()
            messages.success(request, 'Successfully added cat record!')
            return redirect(reverse('cat_detail', args=[cat.id]))
        else:
            messages.error(
                request,
                'Failed to add cat record. Please ensure the form is valid.'
            )
    else:
        form = CatForm()

    template = "cats/add_cat.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_cat(request, cat_id):
    """ edit a cat record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse, ('home'))

    cat = get_object_or_404(Cat, pk=cat_id)

    if request.method == 'POST':
        form = CatForm(request.POST, request.FILES, instance=cat)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated cat record!')
            return redirect(reverse('cat_detail', args=[cat.id]))
        else:
            messages.error(
                request,
                'Failed to update cat record. Please ensure the form is valid.'
            )
    else:
        form = CatForm(instance=cat)
        messages.info(request, f'You are editing {cat.name}')

    template = "cats/edit_cat.html"
    context = {
        'form': form,
        'cat': cat,
    }

    return render(request, template, context)


@login_required
def delete_cat(request, cat_id):
    """ delete a cat record """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owners can do that.')
        return redirect(reverse, ('home'))

    cat = get_object_or_404(Cat, pk=cat_id)
    cat.delete()
    messages.success(request, f'Cat record deleted!')

    return redirect(reverse('cats'))
