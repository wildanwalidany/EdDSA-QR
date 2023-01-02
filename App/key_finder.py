import pprint

from pymongo import MongoClient

# Import ObjectId from bson package (part of PyMongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

class Finder():
    def __init__(self, name):
        self.name = name
        return None
    
    def find(self):

        # Load config from .env file
        MONGODB_URI = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"

        # Connect to MongoDB cluster with MongoClient
        client = MongoClient(MONGODB_URI)

        # Get reference to 'test_db' database
        db = client['test_db']

        # Get reference to 'keys' collection
        keys_collection = db['keys']

        # Query by ObjectId
        document_to_find = {"username": self.name}

        # Retrieves the document matching the query constraint in the 'keys' collection. Assign the result of the operation to a variable named 'result'.
        result = keys_collection.find_one(document_to_find)["public_key"]

        client.close()

        return result