from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
    list_display = (
        'cat', 
        'donation_total', 
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
        'date',
    )

    readonly_fields = (
        'cat', 
        'donation_total', 
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
        'date',
    )

    ordering = ('donor_last_name',)

admin.site.register(Donation, DonationAdmin)
