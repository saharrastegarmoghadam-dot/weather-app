import requests

print("\n--- Weather App ---")

api_key = "2c89b1a4f0dd94151d138623326a1f4c"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nWeather Result:")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°F")
    print("Weather:", data["weather"][0]["description"])

else:
    print("City not found or API error.")