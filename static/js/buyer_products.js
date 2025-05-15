document.addEventListener("DOMContentLoaded", loadAvailableProducts);

async function loadAvailableProducts() {
    const token = localStorage.getItem("token");
    const res = await fetch("/api/products/available/", {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    });

    const list = document.getElementById("product-list");

    if (!res.ok) {
        list.innerHTML = "<p>Failed to load products.</p>";
        return;
    }

    const products = await res.json();

    list.innerHTML = products.map(product => `
        <div class="product-card">
            <h3>${product.name}</h3>
            <p>${product.description}</p>
            <p>Price: £${product.price}</p>
            <p>Stock: ${product.stock}</p>
            <input type="number" id="qty-${product.id}" placeholder="Quantity" min="1">
            <input type="text" id="msg-${product.id}" placeholder="Message (optional)">
            <button onclick="placeOrder(${product.id})">Order</button>
        </div>
    `).join('');
}

async function placeOrder(productId) {
    const token = localStorage.getItem("token");
    const quantity = document.getElementById(`qty-${productId}`).value;
    const message = document.getElementById(`msg-${productId}`).value;

    const res = await fetch("/api/orders/", {
        method: "POST",
        headers: {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            product: productId,
            quantity: quantity,
            message: message
        })
    });

    if (res.ok) {
        alert("Order placed!");
    } else {
        const data = await res.json();
        alert("Order failed: " + JSON.stringify(data));
    }
}
