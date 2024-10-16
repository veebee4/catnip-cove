from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):

    readonly_fields = (
        'donation_number',
        'date',
        'amount',
        'custom_amount',
    )

    fields = (
        'donation_number',
        'date',
        'cat',
        'amount',
        'custom_amount',
        'donor_first_name', 
        'donor_last_name', 
        'donor_email_address', 
        'donor_address_line1', 
        'donor_address_line2', 
        'donor_city_or_town',
        'donor_county',
        'donor_postcode',
        'donor_country',
        'donor_comment',
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
        'donor_country',
    )

    ordering = ('-date',)

admin.site.register(Donation, DonationAdmin)
