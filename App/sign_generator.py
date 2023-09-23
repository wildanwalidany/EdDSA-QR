import nacl.encoding
from nacl.signing import SigningKey
from nacl.encoding import Base64Encoder
import nacl.exceptions  # Import the nacl exceptions module

class SignGenerator:
    def __init__(self, private_key_encoded, message):
        try:
            # Decode the key from a base64 string
            encoder = nacl.encoding.Base64Encoder()
            self.private_key_bytes = encoder.decode(private_key_encoded)

            # Load the signing key from a bytes string
            self.private_key = nacl.signing.SigningKey(self.private_key_bytes)

            # Sign a message with the signing key and encode into base64
            self.signed = self.private_key.sign(message, encoder=nacl.encoding.Base64Encoder())

        except nacl.exceptions.CryptoError as e:
            # Handle cryptographic errors
            print(f"Cryptographic error occurred: {e}")
            raise  # Re-raise the exception for higher-level handling

    def get_signed(self):
        # Return the signature in base64 bytes
        return self.signed