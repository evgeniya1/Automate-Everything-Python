import requests
import os

NEWS_API = os.environ['NEWS_API']

data = requests.get(
    f'https://newsapi.org/v2/everything?qInTitle=united%20states&from=2023-10-01&to=2023-10-02&sortBy=popularity&language=en&apiKey={NEWS_API}'
)

content = data.json()
print(content['status'])
print(content['articles'][0]['title'])
