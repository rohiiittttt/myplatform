document.addEventListener("DOMContentLoaded", fetchUserInfo);

async function fetchUserInfo() {
    const token = localStorage.getItem("token");
    console.log("Token:", token);

    try {
        const response = await fetch("/api/protected/", {
            headers: {
                Authorization: "Bearer " + token
            }
        });

        const data = await response.json();

        if (response.ok && data.username) {
            document.getElementById("welcome-msg").textContent = "Welcome, " + data.username;
        } else {
            document.getElementById("welcome-msg").textContent = "Session expired or unauthorized.";
        }
    } catch (error) {
        console.error("Error fetching user:", error);
        document.getElementById("welcome-msg").textContent = "Network error.";
    }
}

async function loadDashboardMessages() {
    const token = localStorage.getItem("token");
    const chatBox = document.getElementById("dashboard-chat-box");
  
    if (!token || !chatBox) return;
  
    try {
      const res = await fetch('/api/messaging/', {
        headers: {
          'Authorization': 'Bearer ' + token
        }
      });
  
      const data = await res.json();
  
      if (res.ok) {
        const lastFive = data.slice(-5);
        chatBox.innerHTML = lastFive.map(msg => `
          <div class="message-preview">
            <strong>${msg.sender_username || msg.sender}:</strong> ${msg.message_content}
          </div>
        `).join('');
      } else {
        chatBox.innerHTML = "<p>Failed to load messages.</p>";
      }
    } catch (error) {
      chatBox.innerHTML = "<p>Error loading messages.</p>";
      console.error(error);
    }
}  

// async function fetchProducts() {
//     const token = localStorage.getItem("token");
//     const list = document.getElementById("product-list");

//     try {
//         const res = await fetch("/api/products/all-products/", {
//             headers: {
//                 Authorization: "Bearer " + token
//             }
//         });

//         const data = await res.json();

//         if (res.ok) {
//             if (data.length === 0) {
//                 list.innerHTML = "<p>No products yet.</p>";
//             } else {
//                 list.innerHTML = data.map(product => `
//                     <div class="product-card">
//                         <h2>${product.name}</h2>
//                         <p><strong>Price:</strong> $${product.price}</p>
//                         <p><strong>Stock:</strong> ${product.stock}</p>
//                         <p>${product.description}</p>
//                         <button onclick="editProduct(${product.id})">Edit</button>
//                         <button class="delete-btn" onclick="deleteProduct(${product.id})">Delete</button>
//                     </div>
//                 `).join("");
//             }
//         } else {
//             list.innerHTML = "<p >Failed to load products.</p>";
//         }
//     } catch (err) {
//         console.error("Error fetching products:", err);
//         list.innerHTML = "<p>Server error. Please try again later.</p>";
//     }
// }

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
                // 🟣 Get only the last two
                const latestTwo = data.slice(-2).reverse();

                list.innerHTML = latestTwo.map(product => `
                <div class="product-card-message-style">
                    <span><strong>${product.name}</strong></span>
                    <span>Price: $${product.price}</span>
                    <span>Stock: ${product.stock}</span>
                    <button class="delete-btn" onclick="deleteProduct(${product.id})">Delete</button>
                </div>
                `).join('');

            }
        } else {
            list.innerHTML = "<p>Failed to load products.</p>";
        }
    } catch (err) {
        console.error("Error fetching products:", err);
        list.innerHTML = "<p>Server error. Please try again later.</p>";
    }
}

async function deleteProduct(id) {
    const res = await fetch(`/api/products/delete-product/${id}/`, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('token')
        }
    });

    if (res.ok) {
        alert("Product deleted!");
        fetchProducts();
    } else {
        alert("Failed to delete.");
    }
}
async function fetchRentedStorages() {
    const token = localStorage.getItem("token");
    const container = document.getElementById("dashboard-storage-list");

    if (!token || !container) return;

    try {
        const res = await fetch("/api/storage/", {
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });

        const data = await res.json();
        const rented = data
            .filter(storage => storage.status.toLowerCase() === 'rented')
            .slice(-2);

        if (rented.length === 0) {
            container.innerHTML = "<p>No rented storages.</p>";
            return;
        }

        container.innerHTML = rented.map(storage => `
            <div class="storage-row">
                <strong>${storage.storage_location}</strong> — 
                ${storage.storage_capacity} capacity | 
                Occupancy: ${storage.current_occupancy}
            </div>
        `).join("");

    } catch (err) {
        console.error("Failed to load rented storages:", err);
        container.innerHTML = "<p>Error loading storages.</p>";
    }
}


function logout() {
    localStorage.removeItem("token");
    window.location.href = "/login/";
}


document.addEventListener("DOMContentLoaded", () => {
    fetchUserInfo();
    loadDashboardMessages(); // Load messages into dashboard
    fetchProducts();
    fetchRentedStorages();
  });
  