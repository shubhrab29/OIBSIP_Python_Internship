import random
def generate_password():
    print("\n  ∥⩵⩵ Generate Password ⩵⩵∥")

    length = int(input("Enter password length: "))
    print("\nChoose password strength:")
    print("1. Weak")
    print("2. Medium")
    print("3. Strong")

    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        print("\n!!!Warning: Weak passwords are not secure and easy to guess!!!")
    elif choice == "2":
        print("\nMedium strength password selected.")
    elif choice == "3":
        print("\nStrong password selected (Recommended for better security).")
    else:
        print("\nInvalid choice. Defaulting to Strong password.")
        choice = "3"

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"

    if choice == "1":
        characters = letters
    elif choice == "2":
        characters = letters + numbers
    else:
        characters = letters + numbers + symbols

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

def show_menu():
    print("\n==============================")
    print("      PASSWORD GENERATOR      ")
    print("==============================")
    print("1. Generate Password")
    print("2. Exit")
    print("==============================")

# Main program loop
while True:
    show_menu()
    option = input("Enter your choice : ")

    if option == "1":
        generate_password()
        
    elif option == "2":
        print("\nThank you for using Password Generator!!")
        break
    else:
        print("\n!!!Invalid choice. Please try again.!!!")
