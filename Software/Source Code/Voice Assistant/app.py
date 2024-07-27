from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
import requests
from newsapi import NewsApiClient

# Initialize News API client
newsapi = NewsApiClient(api_key='98d677ba5f9d49a79f4bdeedb8875b44')

app = Flask(__name__)
app.secret_key = 'supersecretkey'
CORS(app, supports_credentials=True)  # Ensure CORS supports credentials

# Update the users dictionary to include the admin credentials
users = {
    'user1': 'password1',
    'user2': 'password2',
    'admin': 'admin123'
}

@app.route('/api/login', methods=['POST'])
@cross_origin(supports_credentials=True)  # Enable CORS with credentials support
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True  # Keep session persistent
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/message', methods=['POST'])
@cross_origin(supports_credentials=True)  # Enable CORS with credentials support
def message():
    if 'username' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    data = request.get_json()
    user_message = data.get('message')

    if 'news' in user_message.lower():
        response_message = retrieve_news()
    else:
        response_message = process_message(user_message)

    return jsonify({'response': response_message})

def retrieve_news():
    top_headlines = newsapi.get_top_headlines(country='us')
    if top_headlines['status'] == 'ok':
        articles = top_headlines['articles']
        headlines = [article['title'] for article in articles[:5]]  # Get top 5 headlines
        news = "Here are the top news headlines: " + " ; ".join(headlines)
        return news
    else:
        return "I couldn't retrieve the news at the moment."

def process_message(message):
    return f"Processed message: {message}"

if __name__ == '__main__':
    app.run(debug=True)
