from nacl.signing import SigningKey

        #SIGNING

# Generate a new random signing key                                 PRIVATE KEY
private_key = SigningKey.generate()

print("PRIVATE KEY", private_key)

private_key_bytes = private_key.encode()
print("PRIVATE KEY ENCODED", private_key_bytes)
print(type(private_key_bytes))
print(len(private_key_bytes))

# Sign a message with the signing key                               SIGNATURE
signature = private_key.sign(b"Ini Pesan")
print("SIGNATURE", signature)

# Obtain the verify key for a given signing key                     PUBLIC KEY
public_key = private_key.verify_key                             

# Serialize the verify key to send it to a third party              PUBLIC KEY ENCODED
public_key_bytes = public_key.encode()

print("PUBLIC KEY", public_key_bytes)
print(type(public_key_bytes))