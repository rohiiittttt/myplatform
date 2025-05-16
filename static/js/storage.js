console.log("storage.js loaded");

document.addEventListener("DOMContentLoaded", fetchStorages);

async function fetchStorages() {
    const token = localStorage.getItem("token");

    try {
        const response = await fetch("/api/storage/", {
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            }
        });

        const storages = await response.json();
        const container = document.getElementById("storage-list");

        container.innerHTML = storages.map(storage => `
            <div class="storage-card">
                <h2>${storage.storage_location}</h2>
                <p><strong>Capacity:</strong> ${storage.storage_capacity}</p>
                <p><strong>Occupancy:</strong> ${storage.current_occupancy}</p>
                <p>${storage.description || ''}</p>
                <p><strong>Status:</strong> ${storage.status}</p>
                ${storage.status === "available" ? 
                    `<button class="book-btn" onclick="bookStorage(${storage.id})">Book</button>` 
                    : ""}
            </div>
        `).join("");

    } catch (error) {
        console.error("Error loading storages:", error);
    }
}

async function bookStorage(storageId) {
    const token = localStorage.getItem("token");

    try {
        const response = await fetch(`/api/storage/book/${storageId}/`, {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({})
        });

        if (response.ok) {
            alert("Storage booked successfully!");
            fetchStorages();  // Refresh UI
        } else {
            const data = await response.json();
            alert("Booking failed: " + JSON.stringify(data));
        }
    } catch (error) {
        console.error("Booking error:", error);
        alert("Something went wrong while booking.");
    }
}
