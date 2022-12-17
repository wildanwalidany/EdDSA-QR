import os
import pprint

from pymongo import MongoClient

# Import ObjectId from bson package (part of PyMongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
MONGODB_URI = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'test_db' database
db = client.test_db

# Get reference to 'test_keys' collection
collection = db.test_keys

"======================== FIND DOCUMENT ================================="

# Query by ObjectId
document_to_find = {"name": "Sunari"}

# Retrieves the document matching the query constraint in the 'test_keys' collection
result = collection.find_one(document_to_find)

pprint.pprint(result)
print(result["private_key"])
print(type(result["private_key"]))

"======================== INSERT DOCUMENT ================================="

client.close()