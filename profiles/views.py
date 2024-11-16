from django.shortcuts import render, get_object_or_404
from .models import UserProfile

def profile(request):
    """ display users profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    donations = profile.donations.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'donations': donations,
    }

    return render(request, template, context)
