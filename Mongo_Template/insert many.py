import datetime
import os

from pymongo import MongoClient

# Load config from .env file
MONGODB_URI = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get a reference to 'accounts' collection
accounts_collection = db.accounts

new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
        "last_updated": datetime.datetime.utcnow(),
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
        "last_updated": datetime.datetime.utcnow(),
    },
]

# TODO: Write an expression that inserts the documents in 'new_accounts' into the 'accounts' collection. Assign the result of the insert operation to a variable named 'result'.
result = accounts_collection.insert_many(new_accounts)


document_ids = result.inserted_ids
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

client.close()
