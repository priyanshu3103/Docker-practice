import requests

def fetch_weather_data(api_key, city):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

def main():
    # Replace 'YOUR_API_KEY' with your actual WeatherAPI.com API key
    api_key = '7c490dae61164859aa994009241404'
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(api_key, city)
    if weather_data:
        print("Weather information:")
        print(f"City: {weather_data['location']['name']}")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Weather: {weather_data['current']['condition']['text']}")
        print(f"Humidity: {weather_data['current']['humidity']}%")
        print(f"Wind Speed: {weather_data['current']['wind_kph']} km/h")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
