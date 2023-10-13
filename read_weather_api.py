import requests
import os
import pandas as pd
from geopy.geocoders import Nominatim

API_key = os.environ['OPENWEATHERAPP_API']
units = 'metric'

latitude = 29.8604
longitude = -95.3698

#convert latitude and longitude to city name
geolocator = Nominatim(user_agent="replit_ai")

location = geolocator.reverse(f"{latitude}, {longitude}")
city = location.raw['address']['city']

urtl_lag_log = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&units={units}&appid={API_key}"

r = requests.get(urtl_lag_log)

content = r.json()

# Extracting data from the content JSON
cities = []
times = []
temperatures = []
conditions = []

for forecast in content['list']:
  cities.append(city)
  times.append(forecast['dt_txt'])
  temperatures.append(forecast['main']['temp'])
  conditions.append(forecast['weather'][0]['description'])

# Creating the DataFrame
data = {
    'City': cities,
    'Time': times,
    'Temperature': temperatures,
    'Condition': conditions
}

df = pd.DataFrame(data)
print(df)

#save generated table
df.to_csv('weather_data.txt', index=False)
