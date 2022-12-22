import json
# importing datetime module for now()
import datetime
 

class JsonGEn:
    def __init__(self, name, title, address):
        # using now() to get current time
        current_time = datetime.datetime.now()
        self.name = name
        self.title = title
        self.address = address
        self.timestamp = str(current_time)

    def to_json_bytes(self):
        # Convert the object to a dictionary
        identity_dict = {
            "name": self.name,
            "title": self.title,
            "addressed to": self.address,
            "timestamp": self.timestamp
        }
        
        # Convert the dictionary to a JSON object
        json_object = json.dumps(identity_dict)
        
        # Convert the JSON string to bytes
        json_bytes = bytes(json_object, 'utf-8')
        return json_bytes