from nacl.signing import VerifyKey
from nacl.signing import SigningKey

# Load the signing key from a file
with open("signing_key.bin", "rb") as f:
    signing_key = SigningKey.load(f)
    
signed = b'j\x05\r\xed/(\x05\xdc"0J1~o7E\x8dg\x0c\x1c\xfdA\xdf\x90\xe5\xb1MU\x9d7\xcb\x03\xf0\xac\xe97z\x91\xb9\xcdZ*\xc4X\x91\x878\x00\xb91\x8a&\xdf\xf9\xa9I\xd1\xd2<\xbe|s\xb0\x00Attack at Dawn'
verify_key_bytes = b'\xe3\xd7\x98\x1f]\xdd!v[\xdc\x94\x9cX3\xe1\x16\xce\xe4&V\xd4Q\x94\x96C\xf0\xc5\xac\xb8\xfb\x9ei'
        #VERIFY

# Create a VerifyKey object from a hex serialized public key        #PUBLIC KEY 
verify_key = VerifyKey(verify_key_bytes)
# Check the validity of a message's signature
# The message and the signature can either be passed together, or
# separately if the signature is decoded to raw bytes.
# These are equivalent:
try:
    verify_key.verify(signed)

except:
    print("Signature was forged or corrupt")