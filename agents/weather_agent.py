import requests
from agents.base_agent import BaseAgent

class WeatherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Weather Agent")

    def handle(self, query: str):

        city = query.lower().split("in")[-1].strip()

        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_res = requests.get(geo_url).json()

        if "results" not in geo_res:
            return "❌ Sorry, I couldn't find that city."

        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url).json()

        temperature = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]

        return f"""
🌦 **Weather in {city.title()}**

🌡 Temperature: {temperature}°C  
💨 Wind Speed: {wind} km/h  

Have a great day! ☀️
"""