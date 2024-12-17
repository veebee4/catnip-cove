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

    let form = document.getElementById('donation_form');

    // Handle form submission
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const donationAmount = document.getElementById("id_amount").value;
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
                        address: {
                            postal_code: form.donor_postcode.value,
                          },
                        name: form.donor_first_name.value + " " + form.donor_last_name.value,
                        email: form.donor_email_address.value,
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
});
