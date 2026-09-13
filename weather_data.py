# Weather Data Aggregation
# Dictionary Lab - Bonus

from datetime import datetime

weather_data = {}


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD.")


def get_valid_temperature():
    while True:
        try:
            temperature = float(input("Enter temperature: "))
            return temperature
        except ValueError:
            print("Invalid temperature. Please enter a number.")


def get_valid_humidity():
    while True:
        try:
            humidity = float(input("Enter humidity (%): "))

            if 0 <= humidity <= 100:
                return humidity

            print("Humidity must be between 0 and 100.")

        except ValueError:
            print("Invalid humidity. Please enter a number.")


def add_weather_data():
    city = input("Enter city name: ").strip()
    date = get_valid_date()
    temperature = get_valid_temperature()
    humidity = get_valid_humidity()
    condition = input("Enter weather condition: ").strip()

    if not city or not condition:
        print("City and weather condition cannot be empty.")
        return

    if city not in weather_data:
        weather_data[city] = {}

    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }

    print("Weather data added successfully.")


def search_weather_data():
    city = input("Enter city name to search: ").strip()
    date = get_valid_date()

    if city in weather_data and date in weather_data[city]:
        data = weather_data[city][date]

        print("\nWeather Data")
        print("City:", city)
        print("Date:", date)
        print("Temperature:", data["temperature"])
        print("Humidity:", data["humidity"], "%")
        print("Condition:", data["condition"])
    else:
        print("Weather data not found.")


def update_weather_data():
    city = input("Enter city name to update: ").strip()
    date = get_valid_date()

    if city in weather_data and date in weather_data[city]:
        temperature = get_valid_temperature()
        humidity = get_valid_humidity()
        condition = input("Enter new weather condition: ").strip()

        if not condition:
            print("Weather condition cannot be empty.")
            return

        weather_data[city][date] = {
            "temperature": temperature,
            "humidity": humidity,
            "condition": condition
        }

        print("Weather data updated successfully.")
    else:
        print("Weather data not found.")


def delete_weather_data():
    city = input("Enter city name to delete: ").strip()
    date = get_valid_date()

    if city in weather_data and date in weather_data[city]:
        del weather_data[city][date]

        if not weather_data[city]:
            del weather_data[city]

        print("Weather data deleted successfully.")
    else:
        print("Weather data not found.")


def display_all_weather_data():
    if not weather_data:
        print("No weather data available.")
        return

    print("\nAll Weather Data")

    for city, dates in weather_data.items():
        print(f"\nCity: {city}")

        for date, data in dates.items():
            print(f"  Date: {date}")
            print(f"  Temperature: {data['temperature']}")
            print(f"  Humidity: {data['humidity']}%")
            print(f"  Condition: {data['condition']}")


while True:
    print("\n===== Weather Data Aggregation =====")
    print("1. Add weather data")
    print("2. Search weather data")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Display all weather data")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_weather_data()

    elif choice == "2":
        search_weather_data()

    elif choice == "3":
        update_weather_data()

    elif choice == "4":
        delete_weather_data()

    elif choice == "5":
        display_all_weather_data()

    elif choice == "6":
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 6.")
        