import nacl.encoding
from nacl.signing import SigningKey
from nacl.encoding import Base64Encoder

class SignGenerator:
    def __init__(self, private_key_encoded, message):
        # Decode the key from a base64 string
        encoder = nacl.encoding.Base64Encoder()
        self.private_key_bytes = encoder.decode(private_key_encoded)

        # Load the signing key from a bytes string
        self.private_key = SigningKey(self.private_key_bytes)

        # Sign a message with the signing key and encode into base64                              
        self.signed = self.private_key.sign(message)
        
        return None

    def get_signed(self):
        # Return the signature in base64 bytes
        return self.signed