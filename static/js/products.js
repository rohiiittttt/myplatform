document.addEventListener("DOMContentLoaded", fetchProducts);

async function fetchProducts() {
    const token = localStorage.getItem("token");

    const res = await fetch("/api/products/", {
        headers: {
            Authorization: "Bearer " + token
        }
    });

    const data = await res.json();
    const list = document.getElementById("product-list");

    if (res.ok) {
        list.innerHTML = data.map(product => `
            <div class="product-card">
                <h2>${product.name}</h2>
                <p><strong>Price:</strong> $${product.price}</p>
                <p><strong>Stock:</strong> ${product.stock}</p>
                <p>${product.description}</p>
            </div>
        `).join("");
    } else {
        list.innerHTML = "<p>Failed to load products.</p>";
    }
}

fetch('/api/products/1/edit/', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('token')
    },
    body: JSON.stringify({
        name: 'Updated Name',
        price: 20.0,
        description: 'Updated description',
        stock: 40
    })
});

// Delete product
fetch('/api/products/1/delete/', {
    method: 'DELETE',
    headers: {
        'Authorization': 'Bearer ' + localStorage.getItem('token')
    }
});