def get_bot_response(user_input, user_name):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "greetings"]:
        return f"Hi {user_name}!"
    elif user_input in ["how are you", "how are you doing", "how's it going"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "see you later", "farewell", "exit", "quit"]:
        return f"Goodbye, {user_name}!"
    else:
        return "I don't understand. Try saying 'hello', 'how are you', or 'bye'."

def main():
    print("Welcome to the Simple Chatbot!")
    user_name = input("What's your name? ").strip().title()
    print(f"Nice to meet you, {user_name}!")
    print("You can start chatting now. Type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            print("Bot:", get_bot_response(user_input, user_name))
            break
        print("Bot:", get_bot_response(user_input, user_name))

if __name__ == "__main__":
    main()
