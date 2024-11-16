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

        selected_amount = request.POST.get('amount')
        custom_amount = request.POST.get('custom-amount')
        amount = int(selected_amount) * 100 if selected_amount else int(custom_amount) * 100 if custom_amount else 0

        if not selected_amount and not custom_amount:
            messages.error(request, "Please select or enter an amount.")
        return redirect('donate')

        # get id of cat if one was selected, otherwise default to none
        cat_id = request.POST.get('cat_id')
        cat = get_object_or_404(Cat, id=cat_id) if cat_id else None

        # Add a description for the donation
        description = f"Donation for {cat.name}" if cat else "General Donation"

        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='gbp',
            description=description,
            metadata={
                "cat_id": cat_id,
                "donor_email": request.POST['email']
            }
        )

        # Save the donation to the database
        donation = Donation(
            cat=cat,
            amount=amount / 100,
            custom_amount=amount / 100 if custom_amount else None,
            donor_first_name=request.POST['donor_first_name'],
            donor_last_name=request.POST['donor_last_name'],
            donor_email_address=request.POST['donor_email_address'],
            donor_postcode=request.POST['donor_postcode'],
            stripe_pid=intent.id  #stores the payment id
        )
        donation.save()

    return redirect(reverse('success', args=[int(amount / 100)]))


def successMsg(request, args):
	amount = args
	return render(request, 'donations/success.html', {'amount':amount})