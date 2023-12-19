import requests
import json
from datetime import datetime

# Function to get weather information from OpenWeatherMap API
def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"} 
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Failed to fetch weather data. Status Code: {response.status_code}")
        return None

# Function to suggest the  appropriate clothing based on temperature
def suggest_clothing(temperature):
    if temperature < 10:
        return "It's cold! Wear warm layers."
    elif 10 <= temperature < 20:
        return "It's a nice day. A light jacket or sweater should be enough."
    else:
        return "It's a lovely sunny day! Consider wearing light and breathable clothing."

# Function to write results to a file
def write_to_file(data, filename):
    with open(filename, "w") as file:
        file.write(json.dumps(data, indent=2))

# Main function
def main():
    # API key for OpenWeatherMap (replace with your own key)
    api_key = "090bca33d2ed6ceb0440d599657ea547"

    city = input("Enter the city for weather information: ")

    # Fetching weather data from the OpenWeatherMap API
    weather_data = get_weather(api_key, city)

    if weather_data:
        temperature = weather_data["main"]["temp"]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Suggesting clothing based on temperature
        clothing_suggestion = suggest_clothing(temperature)

        result = {
            "City": city,
            "Temperature": temperature,
            "Time": current_time,
            "Cloth Suggestion": clothing_suggestion,
        }

        print("\nWeather Information:")
        for key, value in result.items():
            print(f"{key}: {value}")
        filename = f"weather_results_{city.lower().replace(' ', '_')}.json"
        write_to_file(result, filename)
        print(f"\nResults saved to {filename}")

# Entry point of the program
if __name__ == "__main__":
    main()
