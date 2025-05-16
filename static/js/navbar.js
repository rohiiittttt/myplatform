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
            document.getElementById("user-name").textContent = data.username;
        } else {
            document.getElementById("user-name").textContent = "";
        }
    } catch (error) {
        console.error("Error fetching user:", error);
        document.getElementById("welcome-msg").textContent = "Network error.";
    }
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "/login/";
}
