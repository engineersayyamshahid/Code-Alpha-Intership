# TASK 4: Basic Chatbot
# Goal: Build a simple rule-based chatbot.
# Scope:
# ● Input from user like: "hello", "how are you", "bye".
# ● Predefined replies like: "Hi!", "I'm fine, thanks!", "Goodbye!".
# Key Concepts Used: if-elif, functions, loops, input/output.


# Basic Chatbot

def chatbot():
    print("🤖 Welcome to AI Chatbot!")
    print("Enter these commands for communication with Bot!")
    print("hello","how are you","what is your name","who made you")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How can I help you?")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How about you?")

        elif user == "what is your name":
            print("Bot: My name is Jarvis.")

        elif user == "who made you":
            print("Bot: I was created using Python. Developer Name : SAYYAM SHAHID")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day. 👋")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot() # function calling