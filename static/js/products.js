document.addEventListener("DOMContentLoaded", fetchProducts);

async function fetchProducts() {
    const token = localStorage.getItem("token");
    const list = document.getElementById("product-list");

    try {
        const res = await fetch("/api/products/all-products/", {
            headers: {
                Authorization: "Bearer " + token
            }
        });

        const data = await res.json();

        if (res.ok) {
            if (data.length === 0) {
                list.innerHTML = "<p>No products yet.</p>";
            } else {
                list.innerHTML = data.map(product => `
                    <div class="product-card">
                        <h2>${product.name}</h2>
                        <p><strong>Price:</strong> $${product.price}</p>
                        <p><strong>Stock:</strong> ${product.stock}</p>
                        <p>${product.description}</p>
                        <button onclick="editProduct(${product.id})">Edit</button>
                        <button class="delete-btn" onclick="deleteProduct(${product.id})">Delete</button>
                    </div>
                `).join("");
            }
        } else {
            list.innerHTML = "<p >Failed to load products.</p>";
        }
    } catch (err) {
        console.error("Error fetching products:", err);
        list.innerHTML = "<p>Server error. Please try again later.</p>";
    }
}

// Edit product (dummy update for now)
async function editProduct(id) {
    const res = await fetch(`/api/products/edit-product/${id}/`, {
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

    if (res.ok) {
        alert("Product updated!");
        fetchProducts(); // reload the list
    } else {
        alert("Failed to update.");
    }
}

// Delete product
async function deleteProduct(id) {
    const res = await fetch(`/api/products/delete-product/${id}/`, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        }
    });

    if (res.ok) {
        alert("Product deleted!");
        fetchProducts(); // reload the list
    } else {
        alert("Failed to delete.");
    }
}
