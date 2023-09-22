import requests
import json
from nacl.encoding import Base64Encoder

# Define a class for making API requests and decoding data
class API_Find():
    # Initialize the class with a username
    def __init__(self, username):
        self.username = username

        # url endpoint
        self.url = "https://data.mongodb-api.com/app/data-zsndf/endpoint/data/v1/action/findOne"

        # Create a payload with the request data in JSON format
        self.payload = json.dumps({
            "dataSource": "Cluster0",
            "database": "test_db",
            "collection": "keys",
            "filter": { "username": self.username },
            "projection": {
                "public_key": 1,
            }
        })

        # header format
        self.headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'ypro1mFVmKud6ljAdy9iwV4CgWbF3GDevpvn5GwRtICndEQSSOvgprjdxa3nTa7L', 
        }

    # Define a method for making a POST request and decoding the response
    def getKey(self):
        try:
            # Send the POST request
            response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
            if response.status_code == 200:
                # Parse the response as JSON
                data = response.json()
                # Extract the public key data from the response
                public_key_data = data['document']['public_key']['Data']
                # Decode the public key data
                public_key_b64 = Base64Encoder.decode(public_key_data)
                print(public_key_b64)

                return public_key_b64
            else:
                print(f'Request failed with status code {response.status_code}')
        except Exception as e:
            print(f'An error occurred: {e}')



# Testing


new_find=API_Find("grizzly")
new_find.getKey()


