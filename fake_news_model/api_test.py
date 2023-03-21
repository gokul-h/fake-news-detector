import requests
import json

local_url = "http://localhost:7071/api/fake_news_deployment"
azure_url = "YOUR_AZURE_URL_PLUS_CODE"

data = [
    {
        "url": "https://edition.cnn.com/2023/03/20/world/ipcc-synthesis-report-climate-intl/index.html",
    }
]

r = requests.post(local_url, json=json.dumps(data))
print(json.dumps(data))
print(r)
print(r.text)

# r = requests.post(azure_url, json=json.dumps(data))
# print(r)
# print(r.text)
