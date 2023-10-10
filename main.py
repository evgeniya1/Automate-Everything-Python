import requests

city_name = 'Denver'
state_code = 'CO'
country_code = 'US'
API_key = '***'

url = f"api.openweathermap.org/data/2.5/forecast?q={city_name},{state_code},{country_code}&appid={API_key}"

url_city = f"api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml&appid={API_key}"

r = requests.get(url_city)

content = r.json()

print(content)
