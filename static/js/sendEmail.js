document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById("contactForm");

    contactForm.addEventListener("submit", function (e) {
        e.preventDefault();

        emailjs.sendForm('service_8psbgm8', 'template_a6e089t', contactForm)
            .then(
                function (response) {
                    console.log('SUCCESS!', response.status, response.text);
                    showToast("Your message has been sent!", "success");
                    contactForm.reset();
                },
                function (error) {
                    console.log('FAILED...', error);
                    showToast("Sorry, something went wrong. Please try again later.", "danger");
                }
            );
    });
});
