# Weather Information System
# Console-based Python Project

def show_menu():
    print("\n====================================")
    print("     WEATHER INFORMATION SYSTEM")
    print("====================================")
    print("1. View Weather by City")
    print("2. View All Available Cities")
    print("3. Get Weather Safety Tips")
    print("4. Exit")
    print("====================================")

# Weather data stored in dictionary
weather_data = {
 "mumbai": {
        "temp": "30°C",
        "condition": "Hot & Humid ☀️",
        "tip": "Stay hydrated and avoid stepping out in peak sunlight."
    },
    "delhi": {
        "temp": "28°C",
        "condition": "Warm & Dusty ☁️",
        "tip": "Wear light clothing and protect yourself from dust."
    },
    "bangalore": {
        "temp": "24°C",
        "condition": "Pleasant ☁️",
        "tip": "Perfect weather for outdoor activities."
    },
    "chennai": {
        "temp": "32°C",
        "condition": "Hot & Humid ☀️",
        "tip": "Drink plenty of water and avoid dehydration."
    },
    "kolkata": {
        "temp": "29°C",
        "condition": "Warm & Humid ☁️",
        "tip": "Carry an umbrella as humidity may increase discomfort."
    },
    "chandigarh": {
        "temp": "25°C",
        "condition": "Pleasant ☁️",
        "tip": "Enjoy the comfortable climate."
    },
    "shimla": {
        "temp": "15°C",
        "condition": "Cold ❄️",
        "tip": "Wear warm clothes to stay comfortable."
    },
    "ahmedabad": {
        "temp": "33°C",
        "condition": "Hot & Dry ☀️",
        "tip": "Avoid direct sunlight and stay hydrated."
    },
    "guwahati": {
        "temp": "27°C",
        "condition": "Humid 🌧️",
        "tip": "Humidity can be high, stay hydrated."
    },
    "shillong": {
        "temp": "18°C",
        "condition": "Cool & Rainy 🌧️",
        "tip": "Carry an umbrella and enjoy the pleasant weather."
    }
}


def view_weather_by_city():
    city = input("\nEnter city name: ").lower()

    if city in weather_data:
        data = weather_data[city]
        print("\n------------------------------------")
        print("City:", city.capitalize())
        print("Temperature:", data["temp"])
        print("Condition:", data["condition"])
        print("Tip:", data["tip"])
        print("------------------------------------")
    else:
        print("\nSorry, weather data for this city is not available.")
        print("Please choose from the available cities.")


def view_all_cities():
    print("\nAvailable Cities:")
    print("------------------------------------")
    for city in weather_data:
        print("-", city.capitalize())
    print("------------------------------------")


def weather_tips():
    print("\nGeneral Weather Safety Tips:")
    print("------------------------------------")
    print("• Drink plenty of water in hot weather.")
    print("• Carry an umbrella during rainy conditions.")
    print("• Wear warm clothes in cold climates.")
    print("• Avoid outdoor activities during extreme heat.")
    print("------------------------------------")


# Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_weather_by_city()
    elif choice == "2":
        view_all_cities()
    elif choice == "3":
        weather_tips()
    elif choice == "4":
        print("\nThank you for using the Weather Information System.")
        break
    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")
