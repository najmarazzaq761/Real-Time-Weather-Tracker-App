#importing necessary libraries
import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import base64

# Function to load and encode image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

# Add background image using custom CSS
def set_background(png_file):
    bin_str = get_base64(png_file)
    bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(bg_img, unsafe_allow_html=True)

# Set the background image
set_background('weather.jpeg') 

# title
st.title("Real-Time Weather Tracker")

#  API key
api_key= 'ed81a88dbb420aad2a9e4a227f2d58e9'

# Get city name from the user
city = st.text_input("Enter city name:")

# URL with metric units to get temperature in Celsius
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# Make the request to the API
response = requests.get(url)
if st.button("Submit"):
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON format

        # Extract weather data
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        desc = data['weather'][0]["description"]
        sunrise_unix = data['sys']['sunrise']
        sunset_unix = data['sys']['sunset']
            
        # converting time into proper format
        sunrise = datetime.fromtimestamp(sunrise_unix).strftime('%I:%M %p')
        sunset = datetime.fromtimestamp(sunset_unix).strftime('%I:%M %p')

        # Display the weather data
        st.write(f"Temperature: {temp} °C")
        st.write(f"Feels Like: {feels_like} °C")
        st.write(f"Wind Speed: {wind_speed} m/s")
        st.write(f"Pressure: {pressure} hPa")
        st.write(f"Humidity: {humidity} %")
        st.write(f"Description: {desc.capitalize()}")
        st.write(f"Sunrise: {sunrise}")
        st.write(f"Sunset: {sunset}")
    else:
        st.write(f'Error: {response.status_code}')
        st.write('Error fetching weather data. Please check the city name or try again later.')
