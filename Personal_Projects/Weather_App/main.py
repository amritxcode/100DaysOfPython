
import requests

def get_weather(city):
    try:
        api_key = "2799da36d23c63bb4bc988841d462408"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code != 200:
            return None,None
        data = response.json()

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        return temp, weather
    
    except:
        return None, None
    
city = input("Enter city: ")

temp, weather = get_weather(city)

if temp is None:
    print("Something went wrong. Check city name or internet.")
else:
    print("\nWeather Report")
    print("----------------------")
    print(f"City: {city.capitalize()}")
    print(f"Temperature in {city.capitalize()}: {temp}°C")
    print(f"Today's weather: {weather.capitalize()}")