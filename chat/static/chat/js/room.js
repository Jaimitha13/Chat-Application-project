// Handle incoming messages
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);

    switch(data.type) {
        case 'chat_message':
            const messageElement = document.createElement('div');
            messageElement.classList.add('message');
            messageElement.innerHTML = `<strong>${data.username}:</strong> ${data.message}`;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight; // auto scroll
            break;

        case 'user_join':
            const joinElement = document.createElement('div');
            joinElement.classList.add('notification');
            joinElement.textContent = `${data.username} joined the chat`;
            chatBox.appendChild(joinElement);
            updateOnlineUsers(data.username, true);
            break;

        case 'user_leave':
            const leaveElement = document.createElement('div');
            leaveElement.classList.add('notification');
            leaveElement.textContent = `${data.username} left the chat`;
            chatBox.appendChild(leaveElement);
            updateOnlineUsers(data.username, false);
            break;
    }
};

// Send message
sendButton.onclick = function() {
    const message = chatMessage.value.trim();
    if (message) {
        chatSocket.send(JSON.stringify({
            'message': message
        }));
        chatMessage.value = '';
    }
};

// Send message on Enter key
chatMessage.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendButton.click();
    }
});

// Update online users list
function updateOnlineUsers(username, isOnline) {
    let userElement = document.querySelector(`li[data-username="${username}"]`);
    
    if (isOnline && !userElement) {
        userElement = document.createElement('li');
        userElement.dataset.username = username;
        userElement.textContent = username;
        onlineUsersList.appendChild(userElement);
    } else if (!isOnline && userElement) {
        userElement.remove();
    }
}

// Handle connection closed
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
