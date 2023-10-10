import requests

data = requests.get(
    'https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-10-01&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c'
)

content = data.json()

print(content['status'])
print(content['message'])
