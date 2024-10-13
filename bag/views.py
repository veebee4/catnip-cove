from django.shortcuts import render

def view_bag(request):
    """ a view to return the shopping bag page """

    return render(request, 'bag/bag.html')
