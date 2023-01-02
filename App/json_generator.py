import json
# importing datetime module for now()
from datetime import datetime
 

class JsonGEn:
    def __init__(self, name, title, address):
        # using now() to get current time
        current_time = datetime.now()
        self.name = name
        self.title = title
        self.address = address
        self.timestamp = str(current_time.strftime("%Y-%m-%d %H:%M:%S"))

    def to_json_bytes(self):
        # Convert the object to a dictionary
        identity_dict = {
            "name": self.name,
            "title": self.title,
            "addressed to": self.address,
            "timestamp": self.timestamp
        }
        
        # Convert the dictionary to a JSON object
        self.json_object = json.dumps(identity_dict)
        
        # Convert the JSON string to bytes
        self.json_bytes = bytes(self.json_object, 'utf-8')
        return self.json_bytes