import nacl.encoding
from nacl.signing import SigningKey
from nacl.encoding import Base64Encoder

# Generate a new random signing key                                 PRIVATE KEY
private_key = SigningKey.generate()

print("PRIVATE KEY", private_key)

private_key_bytes = private_key.encode(encoder=Base64Encoder)
print("PRIVATE KEY ENCODED", private_key_bytes)
print(type(private_key_bytes))
print(len(private_key_bytes))

# The base64 encoded private key
b64_key = "your_base64_encoded_key_goes_here"

# Decode the key from a base64 string
encoder = nacl.encoding.Base64Encoder()
key = encoder.decode(private_key_bytes)


# Load the signing key from a bytes string
signing_key2 = SigningKey(key)

# Sign a message with the signing key                               SIGNATURE
signature = signing_key2.sign(b"Ini Pesan")
print("SIGNATURE", signature)