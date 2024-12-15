document.addEventListener('DOMContentLoaded', function() {
    // Create a Stripe client.
    const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    let clientSecret = $('#id_client_secret').text().slice(1, -1);

    // Initialize Stripe with the public key
    const stripe = Stripe(stripePublicKey);
    // Create an instance of Elements.
    const elements = stripe.elements();
    const style = {
        base: {
            color: '#32325d',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };

    // Create an instance of the card Element.
    const card = elements.create('card', { style: style });
    // Add an instance of the card Element into the `card-element` <div>.
    card.mount('#card-element');
    
    // Handle real-time validation errors from the card Element.
    card.addEventListener('change', function(event) {
        const errorDiv = document.getElementById('card-errors');
        if (event.error) {
            const html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            $(errorDiv).html(html);
        } else {
            errorDiv.textContent = '';
        }
    });

    // Handle form submit
    const form = document.getElementById('payment-form');

    form.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({ 'disabled': true });
        $('#submit-button').attr('disabled', true);
        $('#payment-form').fadeToggle(100);

        const saveInfo = Boolean($('#id-save-info').attr('checked'));
        // From using {% csrf_token %} in the form
        const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        const donationId = document.querySelector('input[name="donation_id"]').value;
        const postData = {
            'csrfmiddlewaretoken': csrfToken,
            'client_secret': clientSecret,
            'save_info': saveInfo,
            'donation_id': donationId,
        };
        const url = '/donations/cache_donation_data/';

        $.post(url, postData).done(function() {
            stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        name: $.trim(form.donor_first_name.value) + ' ' + $.trim(form.donor_last_name.value),
                        email: $.trim(form.donor_email_address.value),
                    },
                }
            }).then(function(result) { 
                if (result.error) {
                    const errorDiv = document.getElementById('card-errors');
                    const html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                    $(errorDiv).html(html);
                    $('#payment-form').fadeToggle(100);
                    card.update({ 'disabled': false });
                    $('#submit-button').attr('disabled', false);
                } else { 
                    if (result.paymentIntent.status === 'succeeded') {
                        form.submit();
                    }
                }
            });
        }).fail(function() {
            // just reload the page, the error will be in django messages
            location.reload();
        });
    });
});
