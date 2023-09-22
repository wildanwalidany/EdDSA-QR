from pymongo import MongoClient
import hashlib
from key_generator import KeyGenerator

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def sign_up(self):
        try:
            # Hash the password
            hashed_password = hashlib.sha256(self.password.encode()).hexdigest()

            # Load URL
            MONGODB_URL = "mongodb+srv://wildanwalidany21:Kenshin77@cluster0.psea199.mongodb.net/?retryWrites=true&w=majority"

            # Connect to the database
            client = MongoClient(MONGODB_URL)
            db = client['test_db']

            # Define keys collection
            keys_collection = db['keys']

            # Create a new KeyGenerator object
            key_generator = KeyGenerator()

            # Get the generated private and public keys
            self.private_key, self.public_key = key_generator.get_binary_keys()

            # Create new keys document
            new_keys = {
                'username': self.username,
                "private_key": self.private_key,
                "public_key": self.public_key,
            }

            # Store the keys in the database
            result1 = keys_collection.insert_one(new_keys)

            # Define user's credentials in the database
            users_collection = db['users']

            # Create new user object
            new_users = {
                'username': self.username,
                'password': hashed_password,
            }

            # Store the user's credentials in the database
            result2 = users_collection.insert_one(new_users)

            # Check if both inserts were successful
            if result1.inserted_id and result2.inserted_id:
                document_id1 = result1.inserted_id
                document_id2 = result2.inserted_id
                print(f"_id of inserted keys document: {document_id1}")
                print(f"_id of inserted users document: {document_id2}")
                print('sign up success')
            else:
                print('Sign up failed. Please try again.')
            # Return the keys
            return self.private_key, self.public_key
        except Exception as e:
            print(f'An error occurred during registration: {e}')
        finally:
            client.close()

    def login(self):
        try:
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
                print('Login failed. Invalid credentials.')
                return None

            # Retrieve the user's signing and verify keys from the database
            keys_collection = db['keys']
            keys = keys_collection.find_one({'username': self.username})
            private_key = keys['private_key']
            public_key = keys['public_key']

            print('Login success')
            return private_key, public_key

        except Exception as e:
            print(f'An error occurred during login: {e}')
        finally:
            client.close()




# Testing  
 
'''
New_acc = User("anya", "passanya")
New_acc.sign_up()

priv, pub = New_acc.login()
print(priv)
print(pub)
'''