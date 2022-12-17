from nacl.signing import SigningKey

import nacl.encoding

class MessageSigner:
    def __init__(self, base64_private_key):
        # Decode the base64-encoded private key
        self.private_key = nacl.signing.SigningKey(
            base64_private_key, encoder=nacl.encoding.Base64Encoder
        )   #ERROR

    def sign(self, message):
        # Use the private key to create a digital signature for the message
        signature = self.private_key.sign(message)

        # Encode the signature in base64 format
        return signature.signature.encode(encoder=nacl.encoding.Base64Encoder)

# Generate a new random signing key                                 PRIVATE KEY
private_key = SigningKey.generate()

print("PRIVATE KEY", private_key)

private_key_bytes = private_key.encode()
print("PRIVATE KEY ENCODED", private_key_bytes)
print(type(private_key_bytes))
print(len(private_key_bytes))


base64_private_key = "..."
signer = MessageSigner(private_key_bytes)

message = b"hello world"
signature = signer.sign(message)
print(signature)
