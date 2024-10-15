from django import forms
from .models import Donation
from cats.models import Cat


class DonationForm(forms.ModelForm):
    AMOUNT_CHOICES = [
        ('5', '£5'),
        ('10', '£10'),
        ('20', '£20'),
        ('30', '£30'),
        ('50', '£50'),
    ]

    cat = forms.ModelChoiceField(queryset=Cat.objects.all(), required=True, label="Select a Cat")
    amount = forms.ChoiceField(choices=AMOUNT_CHOICES, widget=forms.RadioSelect(attrs={'class': 'amount-buttons'}), required=False)
    custom_amount = forms.DecimalField(max_digits=10, decimal_places=2, required=False, min_value=1.00)

    class Meta:
        model = Donation
        fields = [
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
        ]

    def __init__(self, *args, **kwargs):
        cat = kwargs.pop('cat', None)  # Get the cat object from kwargs
        super().__init__(*args, **kwargs)  # Call the parent constructor
        if cat:
            self.fields['cat'].initial = cat  # Set the initial value for the cat field

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        custom_amount = cleaned_data.get('custom_amount')

        if not amount and not custom_amount:
            raise forms.ValidationError("Please select or enter a donation amount.")

        return cleaned_data