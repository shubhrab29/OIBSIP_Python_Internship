#oasis infobyte python project
#two user chat application(console-based)

from datetime import datetime

# List to store chat history
chat_history = []

def show_menu():
    print("\n==============================")
    print("   TWO USER CHAT APPLICATION ")
    print("==============================")
    print("1. Start Chat")
    print("2. View Chat History")
    print("3. Save Chat History to File")
    print("4. Exit")
    print("==============================")

def start_chat():
    user1 = input("Enter name of User 1: ")
    user2 = input("Enter name of User 2: ")

    print("\nChat started between", user1, "and", user2)
    print("Type 'exit' to stop chatting\n")

    while True:
        # User 1 message
        msg1 = input(user1 + ": ")
        if msg1.lower() == "exit":
            print("Chat ended by", user1)
            break

        timestamp1 = datetime.now().strftime("%m-%d %H:%M")
        chat_history.append(f"[{timestamp1}] {user1}: {msg1}")

        # User 2 message
        msg2 = input(user2 + ": ")
        if msg2.lower() == "exit":
            print("Chat ended by", user2)
            break

        timestamp2 = datetime.now().strftime("%m-%d %H:%M")
        chat_history.append(f"[{timestamp2}] {user2}: {msg2}")

def view_chat():
    if not chat_history:
        print("\nNo chat history available.")
    else:
        print("\n========== CHAT HISTORY ==========")
        for message in chat_history:
            print(message)
        print("==================================")

def save_chat():
    if not chat_history:
        print("\nNo chat history to save.")
    else:
        with open("chat_history.txt", "w") as file:
            for message in chat_history:
                file.write(message + "\n")
        print("\nChat history saved to chat_history.txt")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        start_chat()
    elif choice == "2":
        view_chat()
    elif choice == "3":
        save_chat()
    elif choice == "4":
        print("\nThank you for using the chat application.")
        break
    else:
        print("\nInvalid choice. Please try again.")
