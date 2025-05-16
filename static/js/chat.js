document.addEventListener("DOMContentLoaded", () => {
    loadMessages();

    const sendBtn = document.getElementById("send-button");
    if (sendBtn) {
        sendBtn.addEventListener("click", sendMessage);
    }
});

async function loadMessages() {
    const token = localStorage.getItem("token");
    const chatBox = document.getElementById("chat-box");

    if (!token || !chatBox) return;

    try {
        chatBox.innerHTML = "Loading messages...";

        const res = await fetch('/api/messaging/', {  
            headers: {
                'Authorization': 'Bearer ' + token
            }
        });

        const data = await res.json();

        if (res.ok) {
            chatBox.innerHTML = data.map(msg => `
                <div class="message">
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

async function sendMessage() {
    const token = localStorage.getItem("token");
    const recipientUsername = document.getElementById("recipient-id").value;
    const content = document.getElementById("message-input").value;

    if (!token || !recipientUsername || !content) {
        return alert("All fields are required.");
    }

    try {
        const res = await fetch('/api/messaging/', {  
            method: 'POST',
            headers: {
                'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                recipient: recipientUsername,           
                message_content: content,
                message_type: "dm"
            })
        });

        if (res.ok) {
            document.getElementById("message-input").value = '';
            loadMessages();
        } else {
            const errorData = await res.json();
            console.error("Send failed:", errorData);
            alert("Failed to send message.");
        }
    } catch (error) {
        alert("Error sending message.");
        console.error(error);
    }
}
