from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .models import Donation
from .forms import DonationForm
from profiles.models import UserProfile
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


class Donate(generic.View):

    def get(self, request):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        form = None
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                form = DonationForm(
                    initial={
                        "first name": profile.default_first_name,
                        "last name": profile.default_last_name,
                        "email": profile.default_email_address,
                        "postcode": profile.default_postcode,
                    }
                )
            except Profile.DoesNotExist:
                form = DonationForm()
        else:
            form = DonationForm()

        if not stripe_public_key:
            messages.warning(
                request,
                "Stripe public key is missing."
                "Did you forget to set it in your environment?"
            )
        context = {
            "form": form,
            "stripe_public_key": stripe_public_key,
        }
        return render(request, "donations/donate.html", context)

    def post(self, request):
        form = DonationForm(request.POST)
        context = {
                "form": form,
                "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
            }
        if form.is_valid():
            donation = form.save()
            pid = request.POST.get("client_secret").split("_secret")[0]
            donation.stripe_pid = pid
            donation.save()

            if "save_info" in request.POST:
                profile = Profile.objects.get(user=request.user)
                profile.default_first_name = donation.donor_first_name
                profile.default_last_name = donation.donor_last_name
                profile.default_email_address = donation.donor_email_address
                profile.default_postcode = donation.donor_postcode
                profile.save()
            messages.success(request, f"Your donation of £{donation.amount:.2f} was successful!")
            return redirect(reverse('success', args=[donation.donation_number]) + "?is_new_donation=True")
        else:
            messages.error(request, "There was an error with your form. Please double check your information.")
        return render(request, "donations/donate.html", context)


def create_payment_intent(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    donation_amount = json.loads(request.body)["donation_amount"]

    intent = stripe.PaymentIntent.create(
        amount=round(float(donation_amount) * 100),
        currency="gbp",
        )
    return JsonResponse({"client_secret": intent.client_secret})


@require_POST
def cache_donation_data(request):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        save_info = None
        data = json.loads(request.body)
        pid = data["client_secret"].split("_secret")[0]
        donation_amount = data["donation_amount"]
        if "save_info" in data:
            save_info = data["save_info"]

        metadata = {
            "donation_amount": donation_amount,
        }
        if "save_info" in request.POST:
            metadata["save_info"] = save_info
        if request.user.is_authenticated:
            metadata["username"] = request.user
        else:
            metadata["username"] = "AnonymousUser"

        stripe.PaymentIntent.modify(
            pid,
            metadata=metadata,
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now."
            "Please try again later."
        )
        return HttpResponse(content=e, status=400)


def successMsg(request, donation_number):
    """
    Handle successful donations and update user profile if needed
    """
    donation = get_object_or_404(Donation, donation_number=donation_number)
    amount = donation.amount
    save_info = request.session.get('save_info', False)
    is_new_donation_str = request.GET.get('is_new_donation', 'False')
    is_new_donation = is_new_donation_str.lower() == 'true'

    context = {
        'donation': donation,
        'is_new_donation': is_new_donation
    }

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        # Attach the user profile to the donation
        donation.user_profile = profile
        donation.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_first_name': donation.donor_first_name,
                'default_last_name': donation.donor_last_name,
                'default_postcode': donation.donor_postcode,
                'default_email_address': donation.donor_email_address,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
            else:
                messages.error(
                    request,
                    "There was an error saving your profile information."
                )

    return render(request, 'donations/success.html', context)
