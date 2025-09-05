import requests
import os
from dotenv import load_dotenv
load_dotenv()


def get_weather(city):
    API_KEY = os.getenv("API_KEY")
    BASE_URL = os.getenv("BASE_URL")
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        data = response.json()
        print(data)
        main = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main["temp"]
        print(f"Weather in {city} : {weather} , {temperature}C")
    else:
        print("City not found")


city_name = input("Enter city name: ")
get_weather(city_name)
