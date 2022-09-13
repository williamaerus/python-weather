import requests
import json
API_KEY = ""
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name:  ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    coords = data['coord']
    
    weather = data['weather'][0]['description']
    
    temperature = round(data["main"]["temp"] -273.15,2)
    

    print(coords)
    print("weather: ",weather)
    print("temperature: ",temperature, "°C")
else:
    print("an error occured")
