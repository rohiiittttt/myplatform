document.getElementById('create-product-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const token = localStorage.getItem('token');
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = document.getElementById('price').value;
    const stock = document.getElementById('stock').value;

    try {
        const response = await fetch('/api/products/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({ name, description, price, stock })
        });

        const contentType = response.headers.get("content-type");

        if (!response.ok) {
            if (contentType && contentType.includes("application/json")) {
                const data = await response.json();
                alert("Failed to add product: " + (data.detail || JSON.stringify(data)));
            } else {
                const text = await response.text();
                console.error("Server Error:", text);
                alert("Server error occurred. Check console.");
            }
            return;
        }

        alert("Product added successfully!");
        window.location.href = "/products/";
    } catch (err) {
        console.error("Unexpected error:", err);
        alert("Unexpected error: " + err.message);
    }
});
