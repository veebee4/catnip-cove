from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    amount_choices = [
        (None, "Select amount to donate"),  # Placeholder option
        (5, "£5 - Specialist milk for a kitten for 10 days"),
        (10, "£10 - Food for a cat for 50 days"),
        (20, "£20 - Warm blankets for 10 cats"),
        (30, "£30 - Stimulating toys to keep our cats happy"),
        (50, "£50 - Full healthcheck including vaccinations for a cat"),
    ]

    # Adding the ChoiceField with required=False so that the placeholder can be selected initially
    amount = forms.ChoiceField(
        choices=amount_choices, 
        required=False, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    custom_amount = forms.DecimalField(
        max_digits=10, decimal_places=2, min_value=1, required=False
    )

    class Meta:
        model = Donation
        fields = ('amount', 'custom_amount', 'donor_first_name', 'donor_last_name', 'donor_email_address', 'donor_postcode')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'custom_amount': 'Enter Amount Here...',
            'donor_first_name': 'First Name',
            'donor_last_name': 'Last Name',
            'donor_email_address': 'Email Address',
            'donor_postcode': 'Postal Code',
        }

        self.fields['amount'].widget.attrs['autofocus'] = True
        # Iterate over each field in the donation form
        for field in self.fields:
            if field != 'amount':  # Exclude the amount field from the customization
                placeholder = placeholders.get(field)
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'form-control stripe-style-input'
                self.fields[field].label = False  # Removes all labels


    def clean(self):
        cleaned_data = super().clean()
        selected_amount = cleaned_data.get('amount')
        custom_amount = cleaned_data.get('custom_amount')

        # Custom validation to ensure either an amount or custom amount is provided
        if not selected_amount and not custom_amount:
            raise ValidationError('Please select an amount or enter a custom amount.')
        return cleaned_data
