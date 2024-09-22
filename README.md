# Real-Time Weather Tracker App
This is a simple web application that provides real-time weather updates for any city using data from the OpenWeatherMap API. The app allows users to input a city name and get information like the current temperature, wind speed, humidity, and more.

## Features:
- **City-Based Weather Search**: Enter any city and get the real-time weather details.
- **Weather Details**: Temperature, wind speed, humidity, pressure, and description of weather conditions.
- **Sunrise and Sunset Times**: Get the time for sunrise and sunset in a user-friendly format.
- **Responsive Background**: The app has a dynamic background image for a better user experience.

## How It Works:
1. The user inputs the name of a city.
2. The app makes an API call to the [OpenWeatherMap API](https://openweathermap.org/) to fetch real-time weather data.
3. Weather information is displayed, including:
   - Temperature (in °C)
   - Feels like temperature
   - Humidity and pressure
   - Wind speed
   - Weather description
   - Sunrise and sunset times

## Libraries Used:
- **Streamlit**: For creating the web interface.
- **Requests**: For making API requests to fetch weather data.
- **Datetime**: For formatting the sunrise and sunset times.
- **Base64**: To load and encode background images for the app.

## How to Run the App:
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/weather-app.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run weather_app.py
   ```
4. Open your browser and go to the local URL provided (usually `http://localhost:8501`).

## API Key Setup:
- Replace the placeholder API key in the code with your own from [OpenWeatherMap](https://openweathermap.org/).
  
  Example:
  ```python
  api_key = 'your_api_key_here'
  ```
