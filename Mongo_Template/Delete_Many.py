import os
import pprint

from pymongo import MongoClient

# Import ObjectId from bson package (part of PyMongo distribution) to enable querying by ObjectId
from bson.objectid import ObjectId

# Load config from .env file
MONGODB_URI = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter for accounts with balance less than $500
documents_to_delete = {"balance": {"$lt": 500}}

# Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

# TODO: Write an expression that deletes the target accounts. Assign the result of this delete operation to a variable named 'result'.
result = accounts_collection.delete_many(documents_to_delete)

# Search for sample document after delete
print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()
