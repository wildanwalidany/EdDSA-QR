from pymongo import MongoClient

MONGODB_URL = "MONGODB_URI_REMOVED"

client = MongoClient(MONGODB_URL)

for db_name in client.list_database_names():
    print(db_name)

