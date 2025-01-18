from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):

    class Meta:
        model = Donation
        fields = (
            'amount',
            'donor_first_name',
            'donor_last_name',
            'donor_email_address',
            'donor_postcode',
            'message'
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'amount': 'Enter Amount Here...',
            'donor_first_name': 'First Name',
            'donor_last_name': 'Last Name',
            'donor_email_address': 'Email Address',
            'donor_postcode': 'Postal Code',
            'message': (
                'Optionally, add a message to send to the rescue centre '
                'with your donation'
            ),
        }

        self.fields['amount'].widget.attrs['autofocus'] = True
        self.fields['amount'].widget.attrs['min'] = '1'  # Ensures min value is 1 on frontend
        # Iterate over each field in the donation form
        for field in self.fields:
            placeholder = placeholders.get(field)
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'form-control stripe-style-input'
            )
            self.fields[field].label = False  # Removes all labels

    def clean_amount(self):
        """Ensure that the donation amount is at least £1 and positive."""
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be a positive number.")
        if amount < 1:
            raise forms.ValidationError("The minimum donation amount is £1.")
        return amount
