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

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Calculate the average balance of checking and savings accounts with balances of less than $1000.

# Select accounts with balances of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

# Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()