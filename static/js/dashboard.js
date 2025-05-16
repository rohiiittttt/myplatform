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

function logout() {
    localStorage.removeItem("token");
    window.location.href = "/login/";
}


document.addEventListener("DOMContentLoaded", () => {
    fetchUserInfo();
    loadDashboardMessages(); // Load messages into dashboard
  });
  