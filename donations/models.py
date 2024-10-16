import uuid

from django.conf import settings
from django.db import models
from cats.models import Cat


class Donation(models.Model):
    donation_number = models.CharField(max_length=32, null=False, editable=False)
    cat = models.ForeignKey('cats.Cat', on_delete=models.CASCADE, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    custom_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    donor_first_name = models.CharField(max_length=100, blank=False)
    donor_last_name = models.CharField(max_length=100, blank=False)
    donor_email_address = models.EmailField(max_length=100, blank=False)
    donor_address_line1 = models.CharField(max_length=100, blank=True)
    donor_address_line2 = models.CharField(max_length=100, blank=True)
    donor_city_or_town = models.CharField(max_length=100, blank=True)
    donor_county = models.CharField(max_length=50, blank=True)
    donor_postcode = models.CharField(max_length=15, blank=True) 
    donor_country = models.CharField(max_length=50, blank=True)
    donor_comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def _generate_donation_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.donation_number:
            self.donation_number = self._generate_donation_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.donation_number

    def __str__(self):
        return f"Donation of {self.amount} by {self.donor_first_name} {self.donor_last_name}"

