from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    amount_choices = [
        (5, "£5 - Specialist milk for a kitten for 10 days"),
        (10, "£10 - Food for a cat for 50 days"),
        (20, "£20 - Warm blankets for 10 cats"),
        (30, "£30 - Stimulating toys to keep our cats happy"),
        (50, "£50 - Full healthcheck including vaccinations for a cat"),
    ]

    amount = forms.ChoiceField(choices=amount_choices, required=False)
    custom_amount = forms.IntegerField(min_value=1, required=False)

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
        #iterates over each field in the donation form
        for field in self.fields:
            if field != 'amount': #exclude the amount field from from below customisation 
                placeholder = placeholders.get(field) # for all fields except above get placeholders
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'form-control stripe-style-input' #applies two classes to each input on the form
                self.fields[field].label = False #removes all labels