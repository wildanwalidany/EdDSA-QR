from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGODB_URL)

for db_name in client.list_database_names():
    print(db_name)

