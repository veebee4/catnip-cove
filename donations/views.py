from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.db import transaction

from .models import Donation
from cats.models import Cat
from .forms import DonationForm
from profiles.models import UserProfile
import stripe
import json

stripe.api_key = settings.STRIPE_SECRET_KEY


def donate(request):
    cat_id = request.GET.get('cat_id')
    cat = get_object_or_404(Cat, id=cat_id) if cat_id else None
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == 'POST':
        donation_form = DonationForm(request.POST)

        if donation_form.is_valid():
            selected_amount = donation_form.cleaned_data['amount']
            custom_amount = donation_form.cleaned_data['custom_amount']
            donation = donation_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            donation.stripe_pid = pid
            donation.save()

            # Ensure only one of the fields is used
            if selected_amount:
                amount_to_donate = selected_amount
            elif custom_amount:
                amount_to_donate = custom_amount
            else:
                messages.error(request, "Invalid donation amount.")
                return redirect('donate')

             # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST

            amount_to_donate = int(amount_to_donate)
            amount_in_pence = amount_to_donate * 100

            # Create Stripe payment intent
            description = f"Donation for {cat.name}" if cat else "General Donation"
            intent = stripe.PaymentIntent.create(
                amount=amount_in_pence,
                currency=settings.STRIPE_CURRENCY,
                description=description,
                automatic_payment_methods={"enabled": True}
                )

            # Redirect to success page
            return redirect(reverse('success', args=[donation.donation_number]) + "?is_new_donation=True")
        else:
            messages.error(request, "There was an issue with the donation form.")
    else:
        donation_form = DonationForm()

    return render(request, 'donations/donate.html', {
        'cat': cat,
        'donation_form': donation_form,
        'stripe_public_key': stripe_public_key,
    })

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
                messages.error(request, "There was an error saving your profile information.")

    return render(request, 'donations/success.html', context)


@require_POST
def cache_donation_data(request):
    try:
        pid = data["client_secret"].split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        save_info = None
        data = json.loads(request.body)

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
            "Sorry, your payment cannot be processed right now. Please try again later.",
        )

    #     stripe.PaymentIntent.modify(pid, metadata={
    #         'amount': str(donation.amount_to_donate),
    #         'save_info': request.POST.get('save_info'),
    #         'username': request.user,
    #     })
    #     return HttpResponse(status=200)
    # except Exception as e:
    #     messages.error(request, 'Sorry, your payment cannot be \
    #         processed right now. Please try again later.')
    #     return HttpResponse(content=e, status=400)
