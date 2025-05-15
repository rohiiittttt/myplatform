document.addEventListener("DOMContentLoaded", fetchOrders);

async function fetchOrders() {
    const token = localStorage.getItem("token");
    const list = document.getElementById("orders-list");

    if (!token || !list) return;

    try {
        const res = await fetch("/api/orders/", {
            headers: {
                'Authorization': 'Bearer ' + token
            }
        });

        if (!res.ok) {
            list.innerHTML = "<p>Failed to load orders.</p>";
            return;
        }

        const orders = await res.json();

        if (orders.length === 0) {
            list.innerHTML = "<p>No orders found.</p>";
            return;
        }

        list.innerHTML = orders.map(order => `
            <div class="order-card">
                <h3>Order #${order.id}</h3>
                <p><strong>Product:</strong> ${order.product_name || order.product}</p>
                <p><strong>Quantity:</strong> ${order.quantity}</p>
                <p><strong>Status:</strong> ${order.status}</p>
                <p><strong>Buyer:</strong> ${order.buyer_username || order.buyer}</p>
            </div>
        `).join('');
    } catch (error) {
        list.innerHTML = "<p>Error loading orders.</p>";
        console.error("Fetch orders error:", error);
    }
}
