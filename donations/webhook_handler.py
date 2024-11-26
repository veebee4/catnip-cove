from django.http import HttpResponse
from .models import Donation
from cats.models import Cat
from profiles.models import UserProfile

import json
import time
import stripe

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        payload = self.request.body  # Get the raw body of the webhook request
        sig_header = self.request.META['HTTP_STRIPE_SIGNATURE']  # Get the signature from the request header

        try:
            # Verify the event by checking the signature
            event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(content=f"Invalid payload: {str(e)}", status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(content=f"Invalid signature: {str(e)}", status=400)

        # Event is valid, proceed to handle it
        # Now you can handle the event, e.g., 'payment_intent.succeeded'
        if event['type'] == 'payment_intent.succeeded':
            return self.handle_payment_intent_succeeded(event)
        else:
            return self.handle_event(event)


    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        donation_data = intent.metadata.donation_data
        save_info = intent.metadata.save_info
        amount = intent.amount_received

        print(f"Received webhook event: {event}")
        print(f"Amount: {amount}")

    # Check if the amount is too large or improperly formatted
    if isinstance(amount, float):
        amount = int(amount * 100)

        # Get the customer billing details from the intent
        billing_details = intent.charges.data[0].billing_details

        # Get the amount, either from the charge or from custom metadata (if provided)
        custom_amount = intent.metadata.get('custom_amount', None)  # Default to None if not present
        amount = round(intent.charges.data[0].amount / 100, 2)  # Stripe amount (in cents)

        if custom_amount:
            # Use custom_amount if it's provided
            amount = round(float(custom_amount), 2)

        # Clean the customer details (first_name, last_name, email, postcode)
        fields_to_clean = ['first_name', 'last_name', 'email', 'postcode']
        for field in fields_to_clean:
            value = getattr(billing_details, field, None)
            if value == "":
                setattr(billing_details, field, None)

        # Get donation data from metadata
        cat_id = donation_data.get('cat_id', None)  # Retrieve cat_id from metadata (if available)
        general_donation = donation_data.get('general_donation', False)  # Flag for general donation

        # Handle donation for specific cat
        if cat_id:
            try:
                cat = Cat.objects.get(id=cat_id)
            except Cat.DoesNotExist:
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: Cat with ID {cat_id} not found.',
                    status=404)

            # Create a donation linked to the specific cat
            donation = Donation(
                cat=cat,
                amount=amount,
                donor_first_name=billing_details.first_name,
                donor_last_name=billing_details.last_name,
                donor_email_address=billing_details.email,
                donor_postcode=billing_details.postcode,
                # Add any other fields as necessary, like message
            )
            donation.save()

        # Handle general donation (if no cat_id)
        elif general_donation:
            donation = Donation(
                cat=None,  # No specific cat for general donation
                amount=amount,
                donor_first_name=billing_details.first_name,
                donor_last_name=billing_details.last_name,
                donor_email_address=billing_details.email,
                donor_postcode=billing_details.postcode,
                # Add any other fields as necessary, like message
            )
            donation.save()

        else:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: No cat or general donation specified.',
                status=400)

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_first_name = billing_details.first_name
                    profile.default_last_name = billing_details.last_name
                    profile.default_email_address = billing_details.email
                    profile.default_postcode = billing_details.postcode
                    profile.save()
            except UserProfile.DoesNotExist:
                pass  # If profile doesn't exist, don't update anything

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Donation processed successfully',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
