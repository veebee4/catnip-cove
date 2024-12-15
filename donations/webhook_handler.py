# All code taken from Boutique Ado tutorial

from django.http import HttpResponse

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        donation = intent.metadata.donation_amount
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details # updated
        total = round(stripe_charge.donation_amount / 100, 2) # updated

        donation_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                donation = Donation.objects.get(
                    first_name__iexact=billing_details.first_name,
                    last_name__iexact=billing_details.last_name,
                    email_address__iexact=billing_details.email_address,
                    postcode__iexact=billing_details.postcode,
                    total=total,
                    stripe_pid=pid,
                )
                donation_exists = True
                break
            except Donation.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if donation_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified donation already in database',
                status=200)
        else:
            donation = None
            try:
                donation = Donation.objects.create(
                        first_name=billing_details.first_name,
                        last_name=billing_details.last_name,
                        email_address=billing_details.email_address,
                        postcode=billing_details.postcode,
                        total=total,
                        stripe_pid=pid,
                    )
            except Exception as e:
                if donation:
                    donation.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created donation in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)