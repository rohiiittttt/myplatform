document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.querySelector('#username').value.trim();
    const password = document.querySelector('#password').value.trim();

    if (!username || !password) {
        alert("Please fill in all fields.");
        return;
    }

    const response = await fetch('/api/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok) {
        // ✅ Use access token (SimpleJWT format)
        localStorage.setItem('token', data.access);

        // Optional: store refresh if needed
        localStorage.setItem('refresh', data.refresh);

        window.location.href = '/dashboard/';
    } else {
        alert(data.detail || "Login failed.");
    }
});
