import nacl.encoding
from nacl.signing import SigningKey
from nacl.encoding import Base64Encoder

# Generate a new random signing key                                 PRIVATE KEY
random = SigningKey.generate()

private_key_encoded = random.encode(encoder=Base64Encoder)

# Decode the key from a base64 string
encoder = nacl.encoding.Base64Encoder()
private_key_bytes = encoder.decode(private_key_encoded)

# Load the signing key from a bytes string
private_key = SigningKey(private_key_bytes)

# Sign a message with the signing key                               SIGNATURE
signature = private_key.sign(b"wildan")
print("SIGNATURE", signature)

