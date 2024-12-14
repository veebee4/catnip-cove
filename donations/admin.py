from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):

    readonly_fields = (
        'donation_number',
        'date',
        'amount',
        'custom_amount',
        'original_donation',
        'stripe_pid'
    )

    fields = (
        'donation_number',
        'user_profile',
        'date',
        'cat',
        'amount',
        'custom_amount',
        'donor_first_name', 
        'donor_last_name', 
        'donor_email_address', 
        'donor_postcode',
        'original_donation',
        'stripe_pid'
    )

    list_display = (
        'donation_number',
        'date',
        'cat',
        'amount',
        'custom_amount',
        'donor_first_name', 
        'donor_last_name', 
        'donor_email_address', 
        'donor_postcode',
    )

    ordering = ('-date',)

admin.site.register(Donation, DonationAdmin)
