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

# Filter
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}

# Update
add_to_balance = {"$inc": {"balance": 100}}

# Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# TODO: Write an expression that adds to the target account balance by the specified amount. Assign the result of this update operation to a variable named 'result'.
result = accounts_collection.update_one(document_to_update, add_to_balance)

print("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()