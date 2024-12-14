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

stripe.public_api_key = settings.STRIPE_PUBLIC_KEY
stripe.secret_api_key = settings.STRIPE_SECRET_KEY

def donate(request):
    cat_id = request.GET.get('cat_id')
    cat = get_object_or_404(Cat, id=cat_id) if cat_id else None
    form = DonationForm()

    return render(request, 'donations/donate.html', {
        'cat': cat,
        'donation_form': form,
    })


def charge(request):

    if request.method == 'POST':
        donation_form = DonationForm(request.POST)
        
        if donation_form.is_valid():
            selected_amount = donation_form.cleaned_data['amount']
            custom_amount = donation_form.cleaned_data['custom_amount']
            save_info = 'save-info' in request.POST

            if amount is None:
                messages.error(request, "Invalid donation amount.")
                return redirect('donate')

            request.session['save_info'] = save_info

            # Get the cat ID, if applicable
            cat_id = request.POST.get('cat_id')
            cat = get_object_or_404(Cat, id=cat_id) if cat_id else None
            description = f"Donation for {cat.name}" if cat else "General Donation"

            # Create the Stripe payment intent
            try:
                intent = create_stripe_payment_intent(amount, description, {
                "cat_id": cat_id,
                "donor_email_address": donation_form.cleaned_data['donor_email_address'],
            })
            except stripe.error.StripeError as e:
                logger.error(f"Stripe error: {e.user_message}")
                messages.error(request, "Payment processing failed. Please try again.")
                return redirect('donate')

            # Save the donation in the database
            try:
                with transaction.atomic():
                    donation = Donation(
                        cat=cat,
                        amount=amount / 100,
                        custom_amount=custom_amount,
                        donor_first_name=donation_form.cleaned_data['donor_first_name'],
                        donor_last_name=donation_form.cleaned_data['donor_last_name'],
                        donor_email_address=donation_form.cleaned_data['donor_email_address'],
                        donor_postcode=donation_form.cleaned_data['donor_postcode'],
                        stripe_pid=intent.id
                    )
                    donation.save()
            except Exception as e:
                logger.error(f"Error saving donation: {e}")
                messages.error(request, "An error occurred while saving your donation.")
                return redirect('donate')

            # Redirect to success page
            return redirect(reverse('success', args=[donation.donation_number]) + "?is_new_donation=True")
        else:
            messages.error(request, "There was an issue with the donation form.")
            return redirect('donate')

    return redirect('donate')


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


    return render(request, 'donations/success.html', context)
