import requests
import os

city_name = 'Denver'
state_code = 'CO'
country_code = 'US'
API_key = os.environ['OPENWEATHERAPP_API']

url = f"api.openweathermap.org/data/2.5/forecast?q={city_name},{state_code},{country_code}&appid={API_key}"

url_city = f"https://api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml&appid={API_key}?"

lat = 29.8604
lon = -95.3698

urtl_lag_log = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}"

r = requests.get(urtl_lag_log)

content = r.json()

print(content)
