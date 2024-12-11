from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from donations.models import Donation


@login_required
def profile(request):
    """ display users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')

    else:
        form = UserProfileForm(instance=profile)
    donations = profile.donations.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'donations': donations
    }

    return render(request, template, context)


@login_required
def donation_history(request, donation_number):
    donation = get_object_or_404(Donation, donation_number=donation_number)

    template = 'donations/success.html'
    context = {
        'donation': donation,
        'is_new_donation': False
    }

    return render(request, template, context)
