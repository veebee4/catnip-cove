from django.db import models

class Donation(models.Model):
    cat = models.ForeignKey('cats.Cat', on_delete=models.CASCADE, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    donor_first_name = models.CharField(max_length=100)
    donor_last_name = models.CharField(max_length=100)
    donor_email_address = models.EmailField(max_length=100)
    donor_address_line1 = models.CharField(max_length=100, blank=True)
    donor_address_line2 = models.CharField(max_length=100, blank=True)
    donor_city_or_town = models.CharField(max_length=100, blank=True)
    donor_county = models.CharField(max_length=50, blank=True)
    donor_postcode = models.CharField(max_length=15, blank=True) 
    donor_country = models.CharField(max_length=50, blank=True)
    donor_comment = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation of £{self.amount} for {self.cat.name}"

