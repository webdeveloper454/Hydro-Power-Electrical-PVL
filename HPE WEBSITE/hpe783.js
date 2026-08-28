const loginForm = document.getElementById('login-form');
const passwordInput = document.getElementById('password');
const passwordToggle = document.querySelector('.password-toggle');

if (passwordToggle && passwordInput) {
	passwordToggle.addEventListener('click', () => {
		const showingPassword = passwordInput.type === 'text';
		passwordInput.type = showingPassword ? 'password' : 'text';
		passwordToggle.textContent = showingPassword ? 'Show' : 'Hide';
		passwordToggle.setAttribute('aria-label', showingPassword ? 'Show password' : 'Hide password');
		passwordToggle.setAttribute('aria-pressed', String(!showingPassword));
	});
}

if (loginForm) {
	loginForm.addEventListener('submit', (event) => {
		event.preventDefault();
		const email = document.getElementById('email');
		const emailError = document.getElementById('email-error');
		const passwordError = document.getElementById('password-error');
		const status = document.getElementById('form-status');
		const emailIsValid = email.value.trim() && email.validity.valid;
		const passwordIsValid = passwordInput.value.trim().length >= 6;

		emailError.textContent = emailIsValid ? '' : 'Enter a valid email address.';
		passwordError.textContent = passwordIsValid ? '' : 'Password must be at least 6 characters.';
		status.textContent = '';

		if (emailIsValid && passwordIsValid) {
			status.textContent = 'You are successfully signed up!';
		}
	});
}
