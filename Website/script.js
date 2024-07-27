document.addEventListener('DOMContentLoaded', () => {
    // Initialize Virtual Assistant
    initializeVirtualAssistant();

    // Smooth scrolling for navigation links
    document.querySelectorAll('nav ul li a').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Sticky header
    window.addEventListener('scroll', () => {
        const header = document.querySelector('.header-main');
        if (window.scrollY > 50) {
            header.classList.add('sticky');
        } else {
            header.classList.remove('sticky');
        }
    });

    // Add scroll animations
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    }, {
        threshold: 0.1
    });

    document.querySelectorAll('.feature, .blog-post, .testimonial').forEach(element => {
        observer.observe(element);
    });
});

function initializeVirtualAssistant() {
    const projectId = 'YOUR_PROJECT_ID'; // Replace with your actual project ID
    const sessionId = 'YOUR_SESSION_ID'; // Replace with your actual session ID
    const languageCode = 'en-US';

    const sessionClient = new dialogflow.SessionsClient();
    const sessionPath = sessionClient.sessionPath(projectId, sessionId);

    const container = document.getElementById('chat-container');
    container.innerHTML = `
        <div class="chat-messages" id="chat-messages"></div>
        <input type="text" id="user-input" placeholder="Type your message..." autocomplete="off">
    `;

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
        const request = {
            session: sessionPath,
            queryInput: {
                text: {
                    text: query,
                    languageCode: languageCode,
                },
            },
        };

        sessionClient.detectIntent(request)
            .then(responses => {
                const result = responses[0].queryResult;
                addMessageToChat(result.fulfillmentText, 'assistant');
            })
            .catch(err => {
                console.error('ERROR:', err);
                addMessageToChat('Sorry, something went wrong. Please try again.', 'assistant');
            });
    }
}
