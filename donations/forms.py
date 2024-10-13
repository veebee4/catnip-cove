from django import forms

class DonationForm(forms.Form):
    AMOUNT_CHOICES = [
        ('5', '£5'),
        ('10', '£10'),
        ('20', '£20'),
        ('30', '£30'),
        ('50', '£50'),
    ]

    amount = forms.ChoiceField(choices=AMOUNT_CHOICES, widget=forms.RadioSelect(attrs={'class': 'amount-buttons'}), required=False)
    custom_amount = forms.DecimalField(max_digits=10, decimal_places=2, required=False, min_value=1.00)

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get('amount')
        custom_amount = cleaned_data.get('custom_amount')

        if not amount and not custom_amount:
            raise forms.ValidationError("Please select or enter a donation amount.")

        return cleaned_data
