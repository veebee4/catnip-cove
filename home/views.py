from django.shortcuts import render


def index(request):
    """ a view to return the index page """

    return render(request, 'home/index.html')


def contact(request):
    """ a view to return the contact page """

    return render(request, 'home/contact.html')
