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

# Query
documents_to_find = {"balance": {"$gt": 4700}}

# TODO: Write an expression that selects the documents matching the query constraint in the 'accounts; collection. Assign the result of the operation to a variable named 'cursor'.
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()