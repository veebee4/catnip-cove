from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

import time
import stripe

from .models import Donation
from cats.models import Cat
from profiles.models import UserProfile


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, event):
        self.event = event

    # Email confirmation code taken from SJE Collins Animal House Django project - full credit in README
    def _send_confirmation_email(self, donation):
        """Send the user a confirmation email"""
        subject = render_to_string("emails/email_subject.txt")
        body = render_to_string(
            "emails/confirmation_email_body.txt",
            {"donation": donation, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )
        print(f"Sending email to: {donation.donor_email_address}")  # Debugging the email recipient
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [donation.donor_email_address],
        )
        print(f"Email sent to: {donation.donor_email_address}")  # Confirm email was sent

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        save_info = False
        intent = event.data.object
        pid = intent.id
        donation_amount = intent.metadata.donation_amount
        donation_amount = float(donation_amount)
        if "save_info" in intent.metadata:
            save_info = True

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        total = round(stripe_charge.amount / 100, 2)

        print('BILLING: ', billing_details)
        # update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_first_name = donation.donor_first_name
                profile.default_last_name = donation.donor_last_name
                profile.default_email_address = donation.donor_email_address
                profile.default_postcode = donation.donor_postcode
                profile.save()

        # send confirmation email
        donation_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                donation = Donation.objects.get(
                    donor_first_name__iexact=billing_details.name,
                    donor_last_name__iexact=billing_details.name,
                    donor_email_address__iexact=billing_details.email,
                    donor_postcode__iexact=billing_details.address.postal_code,
                    amount=donation_amount,
                    stripe_pid__iexact=pid,
                )
                donation_exists = True
                break
            except Donation.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if donation_exists:
            print("Donation already exists in database, send email")
            self._send_confirmation_email(donation)
            return HttpResponse(
                content=f"Webhook received: {event['type']} | SUCCESS: Verified donation already in database",
                status=200,
            )

        else:
            print("Donation does not exist in database, create donation")
            donation = None
            try:
                donation = Donation.objects.create(
                    donor_first_name=billing_details.name,
                    donor_last_name=billing_details.name,
                    donor_email_address=billing_details.email,
                    donor_postcode=billing_details.address.postal_code,
                    amount=donation_amount,
                    stripe_pid=pid,
                )
                donation.message = (
                    "Donation created from webhook payment_intent.succeeded event."
                )
                donation.save()
                print("Donation created in database, send email")
                self._send_confirmation_email(donation)
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | SUCCESS: Created donation in webhook",
                    status=200,
                )
            except Exception as e:
                print(f"Error creating donation: {e}")
                if donation:
                    donation.delete()
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | ERROR: {e}",
                    status=500,
                )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook from Stripe"""
        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)