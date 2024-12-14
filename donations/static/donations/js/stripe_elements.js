document.addEventListener("DOMContentLoaded", function() {
	// Create a Stripe client.
	const stripe = Stripe('pk_test_51QASgVIRFfIYrlwCBIXBXENo9MSaCGZgqBVInE366lvYT6LTjPqIBWF1uRNXitgCGTiGmoaFKZWakoLikzEJTfoj006Wugd9js');

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
		const displayError = document.getElementById('card-errors');
		if (event.error) {
			displayError.textContent = event.error.message;
		} else {
			displayError.textContent = '';
		}
	});

	// Handle form submission.
	const form = document.getElementById('payment-form');
	form.addEventListener('submit', function(event) {
		event.preventDefault();

		stripe.createToken(card).then(function(result) {
			if (result.error) {
				// Inform the user if there was an error.
				const errorElement = document.getElementById('card-errors');
				errorElement.textContent = result.error.message;
			} else {
				// Send the token to your server.
				stripeTokenHandler(result.token);
			}
		});
	});

	// Submit the form with the token ID.
	function stripeTokenHandler(token) {
		// Insert the token ID into the form so it gets submitted to the server
		const form = document.getElementById('payment-form');
		const hiddenInput = document.createElement('input');
		hiddenInput.setAttribute('type', 'hidden');
		hiddenInput.setAttribute('name', 'stripeToken');
		hiddenInput.setAttribute('value', token.id);
		form.appendChild(hiddenInput);

		// Submit the form
		form.submit();
	}
});
