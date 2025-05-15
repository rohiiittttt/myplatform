document.addEventListener("DOMContentLoaded", loadProducts);

async function loadProducts() {
    const token = localStorage.getItem("token");
    const list = document.getElementById("product-list");

    list.innerHTML = "Loading products...";

    try {
        const res = await fetch("/api/products/available/", {
            headers: { 'Authorization': 'Bearer ' + token }
        });

        const data = await res.json();

        if (res.ok) {
            list.innerHTML = data.map(prod => `
                <div class="card">
                    <h3>${prod.name}</h3>
                    <p>${prod.description}</p>
                    <p><strong>Price:</strong> £${prod.price}</p>
                    <input type="number" id="qty-${prod.id}" placeholder="Quantity" min="1" class="order-input"/>
                    <button onclick="placeOrder(${prod.id})" class="order-btn">Place Order</button>
                </div>
            `).join('');
        } else {
            list.innerHTML = "Failed to load products.";
        }
    } catch (err) {
        console.error(err);
        list.innerHTML = "Error loading products.";
    }
}

async function placeOrder(productId) {
    const token = localStorage.getItem("token");
    const qty = document.getElementById(`qty-${productId}`).value;

    if (!qty || qty < 1) return alert("Please enter a valid quantity.");

    try {
        const res = await fetch("/api/orders/", {
            method: "POST",
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                product: productId,
                quantity: qty,
                message: "Order placed from dashboard"
            })
        });

        if (res.ok) {
            alert("Order placed successfully!");
        } else {
            const err = await res.json();
            alert("Failed to place order: " + JSON.stringify(err));
        }
    } catch (err) {
        console.error(err);
        alert("Error placing order.");
    }
}
