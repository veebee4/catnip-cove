import uuid

from django.conf import settings
from django.db import models
from cats.models import Cat


class Donation(models.Model):
    donation_number = models.CharField(max_length=32, null=False, editable=False)
    cat = models.ForeignKey('cats.Cat', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    custom_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    donor_first_name = models.CharField(max_length=100, blank=False)
    donor_last_name = models.CharField(max_length=100, blank=False)
    donor_email_address = models.EmailField(max_length=100, blank=False)
    donor_postcode = models.CharField(max_length=15, blank=True) 
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
        return f"Donation of {self.amount} by {self.donor_first_name} {self.donor_last_name} for {self.cat.name if self.cat else 'General Donation'}"


