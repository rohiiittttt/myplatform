document.addEventListener("DOMContentLoaded", loadMessages);

async function loadMessages() {
    const token = localStorage.getItem("token");

    const res = await fetch('/api/messaging/', {
        headers: {
            'Authorization': 'Bearer ' + token
        }
    });

    const data = await res.json();
    const chatBox = document.getElementById("chat-box");

    if (res.ok) {
        chatBox.innerHTML = data.map(msg => `
            <div class="message">
                <strong>${msg.sender_username}:</strong> ${msg.content}
            </div>
        `).join('');
    } else {
        chatBox.innerHTML = "<p>Failed to load messages.</p>";
    }
}

async function sendMessage() {
    const token = localStorage.getItem("token");
    const recipientId = document.getElementById("recipient-id").value;
    const content = document.getElementById("message-input").value;

    const res = await fetch('/api/messaging/', {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ recipient: recipientId, content: content })
    });

    if (res.ok) {
        document.getElementById("message-input").value = '';
        loadMessages();
    } else {
        alert("Failed to send message.");
    }
}
