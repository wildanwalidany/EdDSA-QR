import base64
from nacl.signing import SigningKey
import nacl.encoding

# Generate a signing key using PyNaCl
signing_key = SigningKey.generate()

# Encode the signing key as a base64 string
encoded_key = base64.b64encode(signing_key.encode()).decode('utf-8')

# Decode the key from a base64 string
encoder = nacl.encoding.Base64Encoder()
signing_key_bytes = encoder.decode(encoded_key)

# Load the signing key from a bytes string
signing_key2 = SigningKey(signing_key_bytes)

# Sign a message with the signing key                               SIGNATURE
signature = signing_key2.sign(b"Ini Pesan")
print("SIGNATURE", signature)