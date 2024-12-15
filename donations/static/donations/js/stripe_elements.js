document.addEventListener('DOMContentLoaded', function() {
    // Create a Stripe client.
    const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
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

    let form = document.getElementById('payment-form');

    // Handle form submission
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        let donationAmount;
        const selectedAmountElement = document.getElementById("selected_amount");
        const customAmountElement = document.getElementById("custom_amount");

        if (customAmountElement && customAmountElement.value) {
            // Use custom amount if provided
            donationAmount = customAmountElement.value;
        } else if (selectedAmountElement && selectedAmountElement.value) {
            // Use selected amount otherwise
            donationAmount = selectedAmountElement.value;
        } else {
            alert("Please select or enter a donation amount.");
            return; // Stop form submission if no amount is provided
        }

        const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        const saveInfo = Boolean($('#id-save-info').attr('checked'));
        const cacheUrl = "/donations/cache_donation_data/";
        const intentUrl = "/donations/create_payment_intent/";

        try {
            const response = await fetch(intentUrl, {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify({
                    donation_amount: donationAmount,
                }),
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            const data = await response.json();
            const clientSecret = data.client_secret;
            console.log(clientSecret)

            let postData = {
                csrfmiddlewaretoken: csrfToken,
                client_secret: clientSecret,
                message: form.message.value,
                donation_amount: donationAmount,
            };
            if (saveInfo) {
                postData["save_info"] = saveInfo;
            }

            // Post data to cache_donation_data URL
            const cacheResponse = await fetch(cacheUrl, {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,
                },
                body: JSON.stringify(postData),
            });

            if (!cacheResponse.ok) {
                throw new Error("Error caching donation data");
            }

            const paymentResult = await stripe.confirmCardPayment(clientSecret, {
                payment_method: {
                    card: card,
                    billing_details: {
                        first_name: form.first_name.value,
                        last_name: form.last_name.value,
                        email: form.email_address.value,
                        postcode: form.postcode.value,
                    },
                },
            });

            if (paymentResult.error) {
                throw new Error(paymentResult.error.message);
            } else {
                const clientSecretInput = document.createElement("input");
                clientSecretInput.type = "hidden";
                clientSecretInput.name = "client_secret";
                clientSecretInput.value = clientSecret;
                form.appendChild(clientSecretInput);
                form.submit();
            }
        } catch (error) {
            console.error("Error processing payment:", error);
            alert("Error processing payment. Please try again.");
        }
    });
}); // Closing bracket for DOMContentLoaded
