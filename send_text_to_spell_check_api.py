import requests
import json

url = "https://api.languagetool.org/v2/check"

data = {'text': "I goeng to test script", 'language': 'en-US'}

request = requests.post(url, data=data)

result = json.loads(request.text)

print(result)
