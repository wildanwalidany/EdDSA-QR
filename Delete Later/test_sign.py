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

        # Sign a message with the signing key using base64 encoder                             
        self.signature = self.private_key.sign(message, encoder=Base64Encoder)

        return None

    def get_signature(self):
        # Return the signature in byte array
        return self.signature

    # Testing method. Delete later
    def get_private_key(self):
        # Return the private key
        return self.private_key

# Testing
# Generate a new random signing key                                 PRIVATE KEY
random = SigningKey.generate()

private_key_encoded = random.encode(encoder=Base64Encoder)

# Create new object
wildan = SignGenerator(private_key_encoded, b"wildan")

encoded_signature = wildan.get_signature()
# print signature 
print("SIGNATURE", encoded_signature)

# Obtain the verify key for a given signing key
verify_key = wildan.get_private_key().verify_key

# Serialize the verify key to send it to a third party
verify_key_b64 = verify_key.encode(encoder=Base64Encoder)

'======= VERIFY =========='

from nacl.encoding import Base64Encoder
from nacl.signing import VerifyKey

# Create a VerifyKey object from a base64 serialized public key
verify_key = VerifyKey(verify_key_b64, encoder=Base64Encoder)

# Check the validity of a message's signature
# The message and the signature can either be passed together, or
# separately if the signature is decoded to raw bytes.
# These are equivalent:
verify_key.verify(encoded_signature, encoder=Base64Encoder)
signature_bytes = Base64Encoder.decode(encoded_signature.signature)

try:
    verify_key.verify(encoded_signature.message, signature_bytes,
                  encoder=Base64Encoder)
    print("Signature valid")
except:
    print("Signature was forged or corrupt") 
    
'=========== FORGED ======='

# Alter the signed message text
forged = encoded_signature[:-1] + bytes([int(encoded_signature[-1]) ^ 1])
# Will raise nacl.exceptions.BadSignatureError, since the signature check
# is failing
try:
    verify_key.verify(forged)
except:
    print("Signature was forged or corrupt") 