import requests

url = "https://cgi-lib.berkeley.edu/ex.fup.cgi"

file = open("weather_data.txt", 'rb')

req = requests.post(url, files ={"upfile": file})

print(req.text)