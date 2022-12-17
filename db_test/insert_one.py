import datetime
from pymongo import MongoClient
from key_generation import KeyGenerator

"======================== KEY GENERATION ================================="
# Create a new KeyGenerator object
key_generator = KeyGenerator()

# Get the generated private and public keys
private_key = key_generator.private_key_binary
public_key = key_generator.public_key_binary


"======================== INSERT DOCUMENT ================================="
# Load URL
MONGODB_URI = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'test_db' database
db = client.test_db

# Get reference to 'test_keys' collection
collection = db.test_keys

new_account = {
    "name": "Bob",
    "private_key": private_key,
    "public_key": public_key,
    "timestamp": datetime.datetime.utcnow()
}

# insert the 'new_account' document into the 'test_keys' collection
result = collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inserted document: {document_id}")

client.close()
