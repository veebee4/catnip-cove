from django.shortcuts import render, redirect, get_object_or_404
from .forms import DonationForm
from .models import Donation
from cats.models import Cat

def donate(request, cat_id=None): #accepts cat_id as an optional parameter
    cat = None

    # Check if a cat ID is provided in the GET request
    if cat_id:
        cat = get_object_or_404(Cat, id=cat_id)

    if request.method == 'POST':
        form = DonationForm(request.POST, cat=cat)
        if form.is_valid():
            # Use the custom amount if provided, otherwise use the selected amount
            amount = form.cleaned_data['custom_amount'] or form.cleaned_data['amount']

            Donation.objects.create(
                cat=cat,
                amount=amount,
                custom_amount=custom_amount,
                donor_first_name=form.cleaned_data['donor_first_name'],
                donor_last_name=form.cleaned_data['donor_last_name'],
                donor_email_address=form.cleaned_data['donor_email_address'],
                donor_address_line1=form.cleaned_data['donor_address_line1'],
                donor_address_line2=form.cleaned_data['donor_address_line2'],
                donor_city_or_town=form.cleaned_data['donor_city_or_town'],
                donor_county=form.cleaned_data['donor_county'],
                donor_postcode=form.cleaned_data['donor_postcode'],
                donor_country=form.cleaned_data['donor_country'],
                donor_comment=form.cleaned_data['donor_comment'],
            )

            donation.save()
            messages.success(request, ('Your donation was successfully received!'))
            return redirect('donation_success')

    else:
        form = DonationForm(cat=cat)
        messages.error(request, 'Error processing donation')

    return render(request, 'donations/donate.html', {'form': form, 'cat': cat})


