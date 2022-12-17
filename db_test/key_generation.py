import bson
from nacl.signing import SigningKey

"======================== KEY GENERATION ================================="

class KeyGenerator:
    def __init__(self):
        # Generate a new random signing key  
        self.private_key = SigningKey.generate()

        # Convert the private key to a byte array
        self.private_key_bytes = self.private_key.encode()

        # Convert the byte array to a binary object
        self.private_key_binary = bson.binary.Binary(self.private_key_bytes) 

        # Obtain the verify key for a given signing key                     
        self.public_key = self.private_key.verify_key

        # Convert the public key to a byte array
        self.public_key_bytes = self.public_key.encode()

        # Convert the byte array to a binary object
        self.public_key_binary = bson.binary.Binary(self.public_key_bytes) 

# Create a new KeyGenerator object
key_generator = KeyGenerator()

# Get the generated private and public keys
private_key = key_generator.private_key_binary
public_key = key_generator.public_key_binary