document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('chat-container');
    container.innerHTML = `
        <div class="chat-header">
            <h2>Velara Virtual Assistant</h2>
        </div>
        <div class="login-container" id="login-container">
            <input type="text" id="username" placeholder="Username" autocomplete="off">
            <input type="password" id="password" placeholder="Password" autocomplete="off">
            <button id="login-button">Login</button>
            <div id="login-error" style="color: red; display: none;">Invalid credentials, please try again.</div>
        </div>
        <div class="chat-messages" id="chat-messages" style="display: none;"></div>
        <input type="text" id="user-input" placeholder="Type your message..." autocomplete="off" style="display: none;">
    `;

    document.getElementById('login-button').addEventListener('click', () => {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        fetch('http://localhost:5000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'Login successful') {
                document.getElementById('login-container').style.display = 'none';
                document.getElementById('chat-messages').style.display = 'block';
                document.getElementById('user-input').style.display = 'block';
            } else {
                document.getElementById('login-error').style.display = 'block';
            }
        })
        .catch(err => {
            console.error('ERROR:', err);
            document.getElementById('login-error').style.display = 'block';
        });
    });

    document.getElementById('user-input').addEventListener('keypress', function (e) {
        if (e.key === 'Enter' && this.value.trim()) {
            const query = this.value.trim();
            this.value = '';

            addMessageToChat(query, 'user');
            sendMessageToAssistant(query);
        }
    });

    function addMessageToChat(message, sender) {
        const messagesContainer = document.getElementById('chat-messages');
        const messageElement = document.createElement('div');
        messageElement.classList.add('chat-message', sender);
        messageElement.textContent = message;
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function sendMessageToAssistant(query) {
        fetch('http://localhost:5000/api/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: query })
        })
        .then(response => response.json())
        .then(data => {
            addMessageToChat(data.response, 'assistant');
        })
        .catch(err => {
            console.error('ERROR:', err);
            addMessageToChat('Sorry, something went wrong. Please try again.', 'assistant');
        });
    }
});
