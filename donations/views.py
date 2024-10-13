from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonationForm
from .models import Donation


def donate(request):

    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            # Use the custom amount if provided, otherwise use the selected amount
            amount = form.cleaned_data['custom_amount'] or form.cleaned_data['amount']
            
            # Save the donation
            Donation.objects.create(cat=cat, amount=amount)

            # Redirect to a success page or show a message
            return redirect('donation_success')

    else:
        form = DonationForm()

    return render(request, 'donations/donation_page.html', {'form': form})

