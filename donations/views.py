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

@require_POST
def cache_donation_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        donation = Donation.objects.get(id=request.POST.get('donation_id'))
        stripe.PaymentIntent.modify(pid, metadata={
            'donation_id': str(donation.id),
            'amount': str(donation.amount),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def donate(request):
    cat_id = request.GET.get('cat_id')
    cat = get_object_or_404(Cat, id=cat_id) if cat_id else None
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == 'POST':
        donation_form = DonationForm(request.POST)

        if donation_form.is_valid():
            selected_amount = donation_form.cleaned_data['amount']
            custom_amount = donation_form.cleaned_data['custom_amount']

            # Ensure only one of the fields is used
            if selected_amount:
                amount_to_donate = selected_amount
            elif custom_amount:
                amount_to_donate = custom_amount
            else:
                messages.error(request, "Invalid donation amount.")
                return redirect('donate')

            save_info = 'save-info' in request.POST
            request.session['save_info'] = save_info

            amount_to_donate = int(amount_to_donate)
            amount_in_pence = amount_to_donate * 100

            # Create Stripe payment intent
            try:
                description = f"Donation for {cat.name}" if cat else "General Donation"
                intent = stripe.PaymentIntent.create(
                    amount=amount_in_pence,
                    currency='gbp',
                    description=description,
                    automatic_payment_methods={"enabled": True},
                    metadata={
                        "cat_id": cat_id,
                        "donor_email_address": donation_form.cleaned_data['donor_email_address'],
                    }
                )
            except stripe.error.StripeError as e:
                messages.error(request, f"Stripe error: {e.user_message}")
                return redirect('donate')

            # Save the donation to the database
            try:
                with transaction.atomic():
                    donation = Donation(
                        cat=cat,
                        amount=amount_to_donate,  # Store the amount as entered, not in pence
                        donor_first_name=donation_form.cleaned_data['donor_first_name'],
                        donor_last_name=donation_form.cleaned_data['donor_last_name'],
                        donor_email_address=donation_form.cleaned_data['donor_email_address'],
                        donor_postcode=donation_form.cleaned_data['donor_postcode'],
                        stripe_pid=intent.id
                    )
                    donation.save()
            except Exception as e:
                messages.error(request, "An error occurred while saving your donation.")
                return redirect('donate')

            # Redirect to success page
            return redirect(reverse('success', args=[donation.donation_number]) + "?is_new_donation=True")
        else:
            messages.error(request, "There was an issue with the donation form.")
    else:
        donation_form = DonationForm()

        # Create a temporary PaymentIntent for client-side rendering
        client_secret = None
        try:
            intent = stripe.PaymentIntent.create(
                amount=100,  # Temporary amount in pence for rendering the form
                currency='gbp',
                description="Temporary PaymentIntent",
            )
            client_secret = intent.client_secret
        except Exception as e:
            messages.error(request, f"Error creating payment intent: {e}")
            client_secret = None

    return render(request, 'donations/donate.html', {
        'cat': cat,
        'donation_form': donation_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
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
