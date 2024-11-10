function sendEmail(contactForm) {
    emailjs.sendForm('service_8psbgm8', 'template_a6e089t', contactForm)
    .then(
        function(response) {
            console.log('SUCCESS!', response.status, response.text);
            alert("Your message has been sent!");
        },
        function(error) {
            console.log('FAILED...', error);
            alert("Sorry, something went wrong. Please try again later.");
        }
    );
}


