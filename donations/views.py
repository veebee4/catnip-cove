from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from .models import Donation
from cats.models import Cat
import stripe

stripe.api_key = settings.STRIPE_API_KEY


def donate(request):
    return render(request, 'donations/donate.html')


def charge(request):
    
    if request.method == 'POST':
        print('Data:', request.POST)

        selected_amount = request.POST.get('amount')
        custom_amount = request.POST.get('custom-amount')
        amount = int(selected_amount) * 100 if selected_amount else int(custom_amount) * 100 if custom_amount else 0


        customer = stripe.Customer.create(
            name=f"{request.POST['first_name']} {request.POST['last_name']}",
            email=request.POST['email'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
			customer=customer.id,
			amount=amount,
			currency='gbp',
			description="Donation"
			)

    return redirect(reverse('success', args=[int(amount / 100)]))


def successMsg(request, args):
	amount = args
	return render(request, 'donations/success.html', {'amount':amount})