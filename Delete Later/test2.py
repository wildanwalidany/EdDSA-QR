import base64
from nacl.signing import VerifyKey
from nacl.encoding import Base64Encoder

# Decode the base64 encoded verify key
verify_key_bytes = base64.b64decode(verify_key)

# Create a VerifyKey object from the decoded bytes
verify_key = VerifyKey(verify_key_bytes, encoder=Base64Encoder)

# Use the verify() method to verify the signature
try:
    verify_key.verify(signature, message)
    print("The signature is valid.")
except nacl.exceptions.BadSignatureError:
    print("The signature is not valid.")