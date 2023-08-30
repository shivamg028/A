import json
from typing import Final
from model import Weather, dt
import requests

API_KEY: Final[str] = "669de881e4e951f1040a9e9ca2240eb9"
BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city_name: str, mock: bool=True):
    if mock:
        with open("dummy_data.json") as file:
            return json.load(file)
        
    # requesting live data
    payload: dict = {"q": city_name, "appid": API_KEY, "units": "metric"}

    request = requests.get(url=BASE_URL, params=payload)
    data = request.json()


    return data


def get_weather_details(weather):
    days = weather.get("list")

    if not days:
        raise Exception(f"Problem with json: {weather}")

    list_of_weather = []
    for day in days:
        w: Weather = Weather(
            date=dt.fromtimestamp(day.get("dt")),
            details=(details := day.get("main")),
            temp=details.get("temp"),
            weather=(weather := day.get("weather")),
            description=weather[0].get("description"),
        )
        list_of_weather.append(w)
    return list_of_weather
