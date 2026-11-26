const form = document.querySelector('form');
const feedback = document.querySelector('#form-feedback');
const submitButton = form.querySelector('button[type="submit"]');

form.addEventListener('submit', async (event) => {
    event.preventDefault();
    submitButton.disabled = true;
    feedback.textContent = 'Saving task...';
    feedback.dataset.state = '';

    try {
        const response = await fetch(form.action, {
            method: form.method,
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(new FormData(form)),
        });
        const result = await response.json();

        feedback.textContent = result.message;
        feedback.dataset.state = response.ok ? 'success' : 'error';

        if (response.ok) {
            form.reset();
        }
    } catch {
        feedback.textContent = 'Could not submit the task. Please try again.';
        feedback.dataset.state = 'error';
    } finally {
        submitButton.disabled = false;
    }
});
