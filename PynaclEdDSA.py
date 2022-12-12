from nacl.signing import SigningKey
from nacl.signing import VerifyKey

        #SIGNING

# Generate a new random signing key                                 PRIVATE KEY
signing_key = SigningKey.generate()
print("PRIVATE KEY")
print(signing_key)

# Sign a message with the signing key                               SIGNATURE
signed = signing_key.sign(b"Attack at Dawn")
print("SIGNATURE")
print(signed)

# Obtain the verify key for a given signing key                     PUBLIC KEY
verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party              PUBLIC KEY ENCODED
verify_key_bytes = verify_key.encode()

        #VERIFY

# Create a VerifyKey object from a hex serialized public key        #PUBLIC KEY 
verify_key = VerifyKey(verify_key_bytes)
print("PUBLIC KEY")
print(verify_key)
# Check the validity of a message's signature
# The message and the signature can either be passed together, or
# separately if the signature is decoded to raw bytes.
# These are equivalent:
try:
        verify_key.verify(signed)
        print("Signature is valid.")
except:
        print("Signature was forged or corrupt")