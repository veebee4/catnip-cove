from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import DonationForm
from .models import Donation
from cats.models import Cat
import stripe

stripe.api_key = "sk_test_51QASgVIRFfIYrlwCBc5gn8svbvDBHC5AmGFV0iKrPONbfcMTdkt5ejqmEHRnzfn35rkexHvPt6JfTFIX9XgbZtCr00cIhVLqwL"

def donate(request):
    """ a view to return the donation page """

    return render(request, 'donations/donate.html')


def charge(request):


        amount = 5
        if request.method == 'POST':
            print('Data:', request.POST)
        return redirect(reverse('success', args=[amount]))


        # if request.method == 'POST':
		# print('Data:', request.POST)

		# amount = int(request.POST['amount'])

		# customer = stripe.Customer.create(
		# 	email=request.POST['email'],
		# 	name=request.POST['nickname'],
		# 	source=request.POST['stripeToken']
		# 	)

		# charge = stripe.Charge.create(
		# 	customer=customer,
		# 	amount=amount*100,
		# 	currency='usd',
		# 	description="Donation"
		# 	)


def successMsg(request, args):
	amount = args
	return render(request, 'donations/success.html', {'amount':amount})