import requests
from langchain.agents import Tool

def get_weather(city, api_key):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=ja"
    res = requests.get(url)
    data = res.json()
    return f"{city} weather: {data['current']['condition']['text']}, {data['current']['temp_c']}°C"

def get_weather_tool(api_key):
    return Tool(
        name="Weather",
        func=lambda city: get_weather(city, api_key),
        description="Get current weather for a city"
    )
