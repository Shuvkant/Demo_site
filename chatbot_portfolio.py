
# Chatbot Code using Flask for Backend
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def chatbot_response(user_input):
    # Simple rule-based responses
    responses = {
        # Greetings and Farewells
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! How can I help you?",
        "good morning": "Good morning! I hope you have a great day ahead!",
        "good night": "Good night! Sleep tight and take care.",
        "bye": "Goodbye! Feel free to return if you need anything.",
        "how are you": "I'm doing great, thanks for asking! How about you?",
        "thank you": "You're welcome! Let me know if there's anything else I can help with.",
        "what are you doing": "Nothing just listening to the music.",

        # Fun and Casual Chat
        "what's your favorite movie": "I don't watch movies, but I've heard 'The Matrix' is a classic for AI enthusiasts!",
        "tell me a story": "Once upon a time, there was a curious user who loved chatting with a friendly bot... and they lived happily ever after!",
        "sing me a song": "I can't sing, but here's a classic: 'Twinkle, twinkle, little star...'",
        "do you have hobbies": "I enjoy assisting people and learning from our conversations!",
        "can you dance": "I can't dance, but I can cheer you on if you want to dance!",

        # Information and Facts
        "what is machine learning": "Machine learning is a subset of AI where machines are trained to learn patterns from data and make predictions.",
        "what is a computer": "A computer is an electronic device that processes data and performs tasks based on instructions.",
        "how do airplanes fly": "Airplanes fly because of the lift created by their wings as air flows over and under them, along with thrust from engines.",
        "who is the president of the united states": "Let me check the current information for you!",
        "what is space": "Space is the vast, seemingly infinite expanse that exists beyond Earth's atmosphere.",
        "how do i stay healthy": "Eat a balanced diet, exercise regularly, get enough sleep, and manage stress effectively.",

        # Technology and Programming
        "what is an algorithm": "An algorithm is a step-by-step procedure for solving a problem or performing a task.",
        "what is the cloud": "The cloud refers to servers and services accessed over the internet, used for storing and managing data.",
        "what is an api": "An API, or Application Programming Interface, allows two applications to communicate with each other.",
        "how do i debug code": "Start by understanding the error message, use debugging tools, and check your code line by line for mistakes.",
        "what is a loop": "A loop is a programming construct that allows you to repeat a block of code multiple times.",
        "what is git": "Git is a version control system that tracks changes in your code and helps collaborate with others.",

        # Fun Facts and Jokes
        "tell me a fun fact": "Octopuses have three hearts, and two of them stop beating when they swim!",
        "why do programmers prefer dark mode": "Because light attracts bugs!",
        "tell me another joke": "Why do Java developers wear glasses? Because they don't see sharp!",
        "what is your favorite joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",

        # Philosophy and Abstract Topics
        "what is love": "Love is a complex mix of emotions and experiences, but I'm not equipped to feel it.",
        "what is time": "Time is a concept used to measure the progression of events from the past to the future.",
        "what happens after we die": "That's a question many ponder, but no one truly knows the answer.",
        "what is consciousness": "Consciousness is the state of being aware of and able to think about one's surroundings, thoughts, and experiences.",

        # Personal Interaction
        "do you like me": "Of course! I'm here to help and chat with you anytime.",
        "can you be my friend": "I'm always happy to be your virtual friend!",
        "what do you think about humans": "I think humans are fascinating, creative, and endlessly curious.",
        "do you believe in aliens": "I don't have beliefs, but the universe is vast, so who knows what might be out there?",
        "can you help me with my homework": "Sure! Let me know the subject or problem you're working on, and I'll try to assist.",
        "what's your name": "I'm your friendly chatbot, here to assist you!",
        "hello": "Hi there! How can I help you?",
        "hi": "Hello! How can I assist you today?",
        "what's your name": "I'm your friendly chatbot, here to assist you!",
        "i need help": "Sure, I'm here to help. Could you please specify the issue?",
        "how do i reset my password": "To reset your password, click on 'Forgot Password' on the login page and follow the instructions.",
        "what are your working hours": "We are available 24/7 to assist you.",
        "can i talk to a human": "I can connect you to a human agent. Please wait a moment.",
        "what is python": "Python is a versatile, high-level programming language. It's great for beginners and widely used in many fields.",
        "what are data structures": "Data structures are ways of organizing and storing data for efficient access and modification.",
        "how do i create a function in python": "Use the `def` keyword, followed by the function name and parentheses. Example: `def my_function():`",
        "what is recursion": "Recursion is a function calling itself to solve smaller instances of the same problem, with a base case to stop the recursion.",
        "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
        "knock knock": "Who's there?",
        "what's the meaning of life": "42, according to The Hitchhiker's Guide to the Galaxy!",
        "do you have feelings": "Not really, but I do like helping you!",
    }
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I didn't understand that. Can you rephrase?")


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    print("Received data", data)
    user_message = data.get("message", "")
    bot_reply = chatbot_response(user_message)
    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
