from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from donations.models import Donation


def profile(request):
    """ display users profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    donations = profile.donations.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'donations': donations
    }

    return render(request, template, context)


def donation_history(request, donation_number):
    donation = get_object_or_404(Donation, donation_number=donation_number)

    messages.info(request, (
        f'this is a past confirmation for donation number {donation_number}. '
        'A confirmation email was sent on the donation date.'
    ))

    template = 'donation/success.html'
    context = {
        'donation': donation
    }

    return render(request, template, context)