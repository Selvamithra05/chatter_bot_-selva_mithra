from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Simple dictionary of predefined responses, exercises, and motivational quotes
responses = {
    "hello": "Hi there! How are you feeling today?",
    "how are you?": "I'm here to help you relax and feel better. How can I assist you?",
    "what's your name?": "I'm a stress relief chatbot here to help you feel calm.",
    "bye": "Goodbye! Remember to take care of yourself."
}

# Stress relief exercises and resources
exercises = {
    "breathing": "Take a deep breath in through your nose, hold for a few seconds, and then slowly exhale through your mouth. Repeat this 5 times.",
    "relaxation": "Close your eyes, and slowly tense and then relax each muscle group, starting from your toes and working your way up to your head.",
    "visualization": "Imagine a peaceful place where you feel safe and calm. Spend a few minutes visualizing yourself there."
}

# Motivational quotes
quotes = [
    "You are stronger than you think.",
    "Take one step at a time. You don't have to do it all at once.",
    "It's okay to take a break and recharge. You deserve it.",
    "Remember, this too shall pass."
]

# Function to get a response
def get_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for consistency

    # Check for specific stress-related keywords
    if "stressed" in user_input or "anxious" in user_input:
        return "I'm sorry you're feeling this way. Would you like to try a breathing exercise, relaxation technique, or visualization?"
    elif "breathing" in user_input:
        return exercises["breathing"]
    elif "relaxation" in user_input:
        return exercises["relaxation"]
    elif "visualization" in user_input:
        return exercises["visualization"]
    elif "quote" in user_input or "motivation" in user_input:
        return random.choice(quotes)
    
    # Return a predefined response or a default message
    return responses.get(user_input, "Sorry, I don't understand that. Can you tell me more about how you're feeling?")

# Define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
