import requests
import json
url = "https://data.mongodb-api.com/app/data-zsndf/endpoint/data/v1/action/deleteOne"

payload = json.dumps({
    "collection": "book",
    "database": "API",
    "dataSource": "Cluster0",
    "filter": { "author": "Grizzly" }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'ypro1mFVmKud6ljAdy9iwV4CgWbF3GDevpvn5GwRtICndEQSSOvgprjdxa3nTa7L', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
