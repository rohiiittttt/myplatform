function getCSRFToken() {
    const tokenMeta = document.querySelector('meta[name="csrf-token"]');
    return tokenMeta ? tokenMeta.content : '';
}

document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    console.log("Form submit event caught");

    const username = document.querySelector('#username').value.trim();
    const email = document.querySelector('#email').value.trim();
    const password = document.querySelector('#password').value.trim();

    if (!username || !email || !password) {
        alert("Please fill in all fields.");
        return;
    }

    try {
        const response = await fetch('/api/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken()
            },
            body: JSON.stringify({ username, email, password })
        });

        let data;
        try {
            data = await response.json();
        } catch (err) {
            const text = await response.text();
            console.error("Non-JSON response from server:", text);
            alert("Server error: invalid response format.");
            return;
        }

        if (response.ok) {
            window.location.href = '/login/';
        } else {
            alert(data.error || "Registration failed.");
        }
    } catch (error) {
        console.error("Network error:", error);
        alert("Network error. Please try again.");
    }
});
