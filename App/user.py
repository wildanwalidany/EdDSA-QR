import nacl.signing
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
        self.private_key    = key_generator.private_key_binary
        self.public_key     = key_generator.public_key_binary
    
    def sign_up(self):
       # Hash the password
        hashed_password = hashlib.sha256(self.password.encode()).hexdigest()
        # Generate a new signing key
        signing_key = nacl.signing.SigningKey.generate()
        # Generate the corresponding verify key
        verify_key = signing_key.verify_key
        # Connect to the database
        client = MongoClient('mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority')
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
        return signing_key, verify_key

New_acc = User("bob", "passbob")
New_acc.sign_up()