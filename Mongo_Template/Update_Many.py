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
select_accounts = {"account_type": "checking"}

# Update
add_transfer = {"$push": {"transfers_complete": "TR413308000"}}

# TODO: Write an expression that adds the transfer ID number to the 'tranfers_complete' list of each checking account. Assign the result of this update operation to a variable named `result`.
result = accounts_collection.update_many(select_accounts, add_transfer)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
