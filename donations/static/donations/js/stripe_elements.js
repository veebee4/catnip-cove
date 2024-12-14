document.addEventListener('DOMContentLoaded', function() {
    // Create a Stripe client.
    const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
    let clientSecret = document.getElementById('id_client_secret')?.textContent?.slice(1, -1);
    console.log(clientSecret); // Check the output to see if clientSecret is correct

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
    const displayError = document.getElementById('card-errors'); // Initialize this properly
    card.addEventListener('change', function(event) {
        if (event.error) {
            const html = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${event.error.message}</span>
            `;
            displayError.innerHTML = html;
        } else {
            displayError.textContent = '';
        }
    });

    // Handle form submit
    const form = document.getElementById('payment-form');

    form.addEventListener('submit', function (ev) {
        ev.preventDefault();
        card.update({ 'disabled': true });
        document.getElementById('submit-button').disabled = true;

        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: document.querySelector('input[name="donor_first_name"]').value + ' ' +
                          document.querySelector('input[name="donor_last_name"]').value,
                    email: document.querySelector('input[name="donor_email_address"]').value,
                },
            }
        }).then(function (result) { 
            if (result.error) {
                const errorDiv = document.getElementById('card-errors');
                document.getElementById('card-errors').textContent = result.error.message;
                card.update({ 'disabled': false });
                document.getElementById('submit-button').disabled = false;
            } else { 
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    });

});
