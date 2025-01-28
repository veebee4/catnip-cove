document.addEventListener("DOMContentLoaded", function () {
    // Get the form element
    const contactForm = document.getElementById("contactForm");

    // Add an event listener for the submit event
    contactForm.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent page refresh

        // Send the form data using EmailJS
        emailjs.sendForm('service_8psbgm8', 'template_a6e089t', contactForm)
            .then(
                function (response) {
                    console.log('SUCCESS!', response.status, response.text);
                    alert("Your message has been sent!");
                    contactForm.reset(); // Reset the form after success
                },
                function (error) {
                    console.log('FAILED...', error);
                    alert("Sorry, something went wrong. Please try again later.");
                }
            );
    });
});



