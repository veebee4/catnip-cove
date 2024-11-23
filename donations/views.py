from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse

from .models import Donation
from cats.models import Cat
from .forms import DonationForm
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
import stripe

stripe.api_key = settings.STRIPE_API_KEY

def donate(request):
    cat_id = request.GET.get('cat_id')
    cat = get_object_or_404(Cat, id=cat_id) if cat_id else None
    donation_form = DonationForm()

    return render(request, 'donations/donate.html', {
        'cat': cat,
        'donation_form': donation_form
    })


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST) # remove this before production

        # Handle form submission with the selected amount or custom amount
        donation_form = DonationForm(request.POST)
        
        if donation_form.is_valid():
            selected_amount = donation_form.cleaned_data['amount']
            custom_amount = donation_form.cleaned_data['custom_amount']
            save_info = 'save-info' in request.POST

            request.session['save_info'] = save_info

            # Determine the donation amount
            if custom_amount:
                try:
                    amount = int(custom_amount) * 100
                except ValueError:
                    messages.error(request, "Invalid custom donation amount.")
                    return redirect('donate')
            elif selected_amount:
                try:
                    amount = int(selected_amount) * 100
                except ValueError:
                    messages.error(request, "Invalid predefined donation amount.")
                    return redirect('donate')
            else:
                messages.error(request, "Please select or enter an amount.")
                return redirect('donate')

            # Get the cat ID, if available
            cat_id = request.POST.get('cat_id')
            cat = get_object_or_404(Cat, id=cat_id) if cat_id else None

            # Create the Stripe payment intent
            description = f"Donation for {cat.name}" if cat else "General Donation"

            try:
                intent = stripe.PaymentIntent.create(
                    amount=amount,
                    currency='gbp',
                    description=description,
                    metadata={
                        "cat_id": cat_id,
                        "donor_email_address": donation_form.cleaned_data['donor_email_address'],
                    }
                )
            except stripe.error.StripeError as e:
                # Handle Stripe errors (like invalid payment info)
                messages.error(request, f"Stripe error: {e.user_message}")
                return redirect('donate')

            # Save the donation in the database
            donation = Donation(
                cat=cat,
                amount=amount / 100,
                custom_amount=custom_amount,
                donor_first_name=donation_form.cleaned_data['donor_first_name'],
                donor_last_name=donation_form.cleaned_data['donor_last_name'],
                donor_email_address=donation_form.cleaned_data['donor_email_address'],
                donor_postcode=donation_form.cleaned_data['donor_postcode'],
                stripe_pid=intent.id  # Store the payment ID from Stripe
            )
            donation.save()

            return redirect(reverse('success', args=[donation.donation_number]))
        else:
            # If the form is not valid, return to the donation page & display error
            messages.error(request, "There was an issue with your donation form.")
            return redirect('donate')

    return redirect('donate')


def successMsg(request, donation_number):
    """
    Handle successful checkouts and update user profile if needed
    """
    donation = get_object_or_404(Donation, donation_number=donation_number)
    amount = donation.amount
    save_info = request.session.get('save_info', False)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        # Attach the user profile to the order
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

    return render(request, 'donations/success.html', {'amount': amount})
