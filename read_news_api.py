import requests

data = requests.get(
    'https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-10-01&to=2023-10-02&sortBy=popularity&language=en&apiKey=853e0c4188634ecfb962f0de8c7be1ce'
)

content = data.json()
print()
print(content['status'])
print(content['articles'][0]['title'])
