from django.contrib import admin
from .models import Donation


class DonationAdmin(admin.ModelAdmin):

    readonly_fields = (
        'donation_number',
        'date',
        'amount',
        'message',
        'stripe_pid'
    )

    fields = (
        'donation_number',
        'user_profile',
        'date',
        'amount',
        'donor_first_name',
        'donor_last_name',
        'donor_email_address',
        'donor_postcode',
        'message',
        'stripe_pid'
    )

    list_display = (
        'donation_number',
        'date',
        'amount',
        'donor_first_name',
        'donor_last_name',
        'donor_email_address',
        'donor_postcode',
        'message',
    )

    ordering = ('-date',)


admin.site.register(Donation, DonationAdmin)
