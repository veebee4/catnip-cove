from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .models import Donation
from cats.models import Cat
from .forms import DonationForm
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
        print('Data:', request.POST)

        # Handle form submission with the selected amount or custom amount
        donation_form = DonationForm(request.POST)
        
        if donation_form.is_valid():
            selected_amount = donation_form.cleaned_data['amount']
            custom_amount = donation_form.cleaned_data['custom_amount']

            # Determine the donation amount
            if custom_amount:
                amount = custom_amount * 100 
            elif selected_amount:
                amount = selected_amount * 100
            else:
                messages.error(request, "Please select or enter an amount.")
                return redirect('donate')

            # Get the cat ID, if available
            cat_id = request.POST.get('cat_id')
            cat = get_object_or_404(Cat, id=cat_id) if cat_id else None

            # Create the Stripe payment intent
            description = f"Donation for {cat.name}" if cat else "General Donation"
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='gbp',
                description=description,
                metadata={
                    "cat_id": cat_id,
                    "donor_email": donation_form.cleaned_data['donor_email_address']
                }
            )

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

            return redirect(reverse('success', args=[int(amount / 100)]))
        else:
            # If the form is not valid, return to the donation page & display error
            messages.error(request, "There was an issue with your donation form.")
            return redirect('donate')

    return redirect('donate')


def successMsg(request, args):
    amount = args
    return render(request, 'donations/success.html', {'amount': amount})
