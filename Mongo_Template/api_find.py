import requests
import json

url = "https://data.mongodb-api.com/app/data-zsndf/endpoint/data/v1/action/findOne"

payload = json.dumps({
    "dataSource": "Cluster0",
    "database": "test_db",
    "collection": "keys",
    "filter": { "username": "grizzly" },
    "projection": {
        "public_key": 1,
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'ypro1mFVmKud6ljAdy9iwV4CgWbF3GDevpvn5GwRtICndEQSSOvgprjdxa3nTa7L', 
}

response = requests.request("POST", url, headers=headers, data=payload)


if response.status_code == 200:
    data = response.json()
    print(data)
    public_key_data = data['document']['public_key']['Data']
    print(public_key_data)
    