import streamlit as st
import requests

# OpenWeatherMap API Key (Replace with your own key)
API_KEY = "4ab4e82123c0f13c23eb79264788495e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit UI
st.title("🌤️ Weather App")
st.write("Enter a city name to get the current weather details.")

# User input
city = st.text_input("Enter City Name:", "")

if city:
    weather_data = get_weather(city)
    if weather_data:
        st.subheader(f"Weather in {city}")
        st.write(f"🌡️ Temperature: {weather_data['main']['temp']}°C")
        st.write(f"🌬️ Wind Speed: {weather_data['wind']['speed']} m/s")
        st.write(f"💧 Humidity: {weather_data['main']['humidity']}%")
        st.write(f"⛅ Condition: {weather_data['weather'][0]['description'].capitalize()}")
    else:
        st.error("City not found. Please enter a valid city name.")

