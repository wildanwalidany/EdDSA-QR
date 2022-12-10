from nacl.signing import SigningKey

        #SIGNING

# Generate a new random signing key                                 PRIVATE KEY
signing_key = SigningKey.generate()

# Sign a message with the signing key                               SIGNATURE
signed = signing_key.sign(b"Attack at Dawn")
print("SIGNATURE")
print(signed)

# Obtain the verify key for a given signing key                     PUBLIC KEY
verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party              PUBLIC KEY ENCODED
verify_key_bytes = verify_key.encode()
print("PUBLIC KEY")
print(verify_key_bytes)