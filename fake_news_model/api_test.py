import requests
import json

local_url = "http://localhost:7071/api/fake_news_deployment"
azure_url = "YOUR_AZURE_URL_PLUS_CODE"

data = [
    {
        'text': """Sample text here display to just inform its just fake""",
    }
]

r = requests.post(local_url, json=json.dumps(data))
print(r)
print(r.text)

# r = requests.post(azure_url, json=json.dumps(data))
# print(r)
# print(r.text)
