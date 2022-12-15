from pymongo import MongoClient
import hashlib
from key_generator import KeyGenerator

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Create a new KeyGenerator object
        key_generator = KeyGenerator()

        # Get the generated private and public keys
        self.private_key, self.public_key   = key_generator.get_keys()
    
    def sign_up(self):
       # Hash the password
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

        # Load URL
        MONGODB_URL = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"
        # Connect to the database
        client = MongoClient(MONGODB_URL)
        db = client['test_db']
        # Store the keys in the database
        keys_collection = db['keys']

        #create new keys document
        new_keys = {
            'username': self.username,
            "private_key": self.private_key,
            "public_key": self.public_key,
        }

        result1 = keys_collection.insert_one(new_keys)
        
        # Store the user's credentials in the database
        users_collection = db['users']

        new_users = {
            'username': self.username,
            'password': hashed_password,
        }

        result2 = users_collection.insert_one(new_users)

        # Create result object
        document_id1 = result1.inserted_id
        document_id2 = result2.inserted_id
        print(f"_id of inserted keys document: {document_id1}")
        print(f"_id of inserted users document: {document_id2}")
        client.close()
        # Return the keys
        return self.private_key, self.public_key

    def login(self):
        # Hash the password
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        # Load URL
        MONGODB_URL = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"
        # Connect to the database
        client = MongoClient(MONGODB_URL)
        db = client['test_db']

        # Verify the user's credentials
        users_collection = db['users']
        user = users_collection.find_one({'username': self.username, 'password': hashed_password})
        if user is None:
            return None
        # Retrieve the user's signing and verify keys from the database
        keys_collection = db['keys']
        keys = keys_collection.find_one({'username': self.username})
        private_key = keys['private_key']
        public_key = keys['public_key']

        client.close()
        # Return the keys
        return private_key, public_key



# Testing      
New_acc = User("jane", "passjane")
New_acc.sign_up()

priv, pub = New_acc.login()
print(priv)
print(pub)
