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
import logging

stripe.api_key = settings.STRIPE_SECRET_KEY
logger = logging.getLogger(__name__)

# Constants for messages
STRIPE_KEY_MISSING_MSG = (
    "Stripe public key is missing. "
    "Did you forget to set it in your environment?"
)
FORM_ERROR_MSG = (
    "There was an error with your form. "
    "Please double-check your information."
)
DONATION_SUCCESS_MSG = "Your donation of £{amount:.2f} was successful!"
PAYMENT_ERROR_MSG = (
    "Sorry, your payment cannot be processed right now. "
    "Please try again later."
)
PROFILE_SAVE_ERROR_MSG = "There was an error saving your profile information."


def get_user_profile(user):
    """
    Helper function to get the user's profile and return default values.
    """
    try:
        profile = UserProfile.objects.get(user=user)
        return {
            "first_name": profile.default_first_name,
            "last_name": profile.default_last_name,
            "email": profile.default_email_address,
            "postcode": profile.default_postcode,
            "profile": profile,
        }
    except UserProfile.DoesNotExist:
        return None


class Donate(generic.View):
    def get(self, request):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY

        # Get initial data if the user is authenticated
        initial_data = {}
        if request.user.is_authenticated:
            profile_data = get_user_profile(request.user)
            if profile_data:
                initial_data = {
                    "first_name": profile_data["first_name"],
                    "last_name": profile_data["last_name"],
                    "email": profile_data["email"],
                    "postcode": profile_data["postcode"],
                }

        form = DonationForm(initial=initial_data)

        if not stripe_public_key:
            messages.warning(request, STRIPE_KEY_MISSING_MSG)

        context = {
            "form": form,
            "stripe_public_key": stripe_public_key,
        }
        return render(request, "donations/donate.html", context)

    def post(self, request):
        form = DonationForm(request.POST)
        stripe_public_key = settings.STRIPE_PUBLIC_KEY

        if form.is_valid():
            # Save the donation instance
            donation = form.save(commit=False)
            pid = request.POST.get("client_secret", "").split("_secret")[0]
            donation.stripe_pid = pid
            donation.save()

            # Save user information if 'save_info' is checked
            save_info = request.POST.get("save_info", "off") == "on"
            if save_info and request.user.is_authenticated:
                try:
                    # Fetch the user's profile
                    profile = UserProfile.objects.get(user=request.user)
                    # Update profile with the donation form data
                    profile.default_first_name = donation.donor_first_name
                    profile.default_last_name = donation.donor_last_name
                    profile.default_email_address = (
                        donation.donor_email_address
                    )
                    profile.default_postcode = donation.donor_postcode
                    profile.save()
                except UserProfile.DoesNotExist:
                    messages.warning(
                        request,
                        "Could not save your information. "
                        "User profile not found."
                    )

            # Success message and redirect
            messages.success(
                request,
                f"Your donation of £{donation.amount:.2f} was successful!"
            )
            return redirect(
                reverse(
                    "success",
                    args=[donation.donation_number]) + "?is_new_donation=True"
            )
        else:
            # Error handling if the form is invalid
            messages.error(
                request,
                "There was an error with your form. "
                "Please double-check your information."
            )

        # Re-render the donation form with errors
        context = {
            "form": form,
            "stripe_public_key": stripe_public_key,
        }
        return render(request, "donations/donate.html", context)


def create_payment_intent(request):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        donation_amount = json.loads(request.body).get("donation_amount", 0)

        if not donation_amount or float(donation_amount) <= 0:
            return JsonResponse(
                {
                    "error": "Invalid donation amount. "
                    "Please enter a valid number."
                },
                status=400,
            )

        intent = stripe.PaymentIntent.create(
            amount=round(float(donation_amount) * 100),
            currency="gbp",
        )
        return JsonResponse({"client_secret": intent.client_secret})
    except Exception as e:
        logger.error(f"Error creating payment intent: {e}")
        return JsonResponse(
            {"error": "An error occurred while creating the payment intent."},
            status=500,
        )


@require_POST
def cache_donation_data(request):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        data = json.loads(request.body)
        pid = data["client_secret"].split("_secret")[0]
        save_info = data.get("save_info", False)

        # Ensure all metadata values are strings
        metadata = {
            "donation_amount": str(data.get("donation_amount", "")),
            "save_info": str(save_info),
            "username": (
                str(request.user.username)
                if request.user.is_authenticated
                else "AnonymousUser"
            ),
        }

        stripe.PaymentIntent.modify(pid, metadata=metadata)
        return HttpResponse(status=200)

    except Exception as e:
        logger.error(f"Error caching donation data: {e}")
        messages.error(
            request,
            "Sorry, there was an issue processing your donation. "
            "Please try again later."
        )
        return HttpResponse(content=e, status=400)


def successMsg(request, donation_number):
    donation = get_object_or_404(Donation, donation_number=donation_number)
    save_info = request.session.get("save_info", False)
    is_new_donation = (
        request.GET.get("is_new_donation", "false").lower() == "true"
    )

    if request.user.is_authenticated:
        profile_data = get_user_profile(request.user)
        if profile_data:
            profile = profile_data["profile"]
            donation.user_profile = profile
            donation.save()

            # Save user info if requested
            if save_info:
                profile.default_first_name = donation.donor_first_name
                profile.default_last_name = donation.donor_last_name
                profile.default_email_address = donation.donor_email_address
                profile.default_postcode = donation.donor_postcode
                profile.save()

    context = {
        "donation": donation,
        "is_new_donation": is_new_donation,
    }
    return render(request, "donations/success.html", context)
