from nacl.encoding import Base64Encoder
from nacl.signing import VerifyKey

class Verifier():
    def __init__(self, public_key_b64, encoded_signature):
        # Create a VerifyKey object from a base64 serialized public key
        public_key = VerifyKey(public_key_b64, encoder=Base64Encoder)

        # Check the validity of a message's signature
        public_key.verify(encoded_signature, encoder=Base64Encoder)
        self.signature_bytes = Base64Encoder.decode(encoded_signature.signature)

        return None

    def result(self):
        try:
            self.public_key.verify(self.encoded_signature.message, self.signature_bytes,
                  encoder=Base64Encoder)
            print("Signature valid")
            return True
        
        except:
            print("Signature was forged or corrupt")
            return False 

# Testing
import nacl.encoding
from nacl.signing import SigningKey
from nacl.encoding import Base64Encoder
from sign_generator import SignGenerator

# Generate a new random signing key                                 PRIVATE KEY
random = SigningKey.generate()

private_key_encoded = random.encode(encoder=Base64Encoder)

# Create new object
wildan = SignGenerator(private_key_encoded, b"wildan")
encoded_signature = wildan.get_signature()
# print signature 
print("SIGNATURE", encoded_signature)

# Obtain the verify key for a given signing key
verify_key = wildan.private_key.verify_key

# Serialize the verify key to send it to a third party
verify_key_b64 = verify_key.encode(encoder=Base64Encoder)

'========================================'

# new_verify = Verifier(verify_key_b64, encoded_signature)
# result = new_verify.result()
# print('RESULT', result)


'==========================================='
class VerifierTest():
    def __init__(self, public_key_b64, encoded_signature):
        
        # Create a VerifyKey object from a base64 serialized public key
        self.public_key = VerifyKey(public_key_b64, encoder=Base64Encoder)

        # Check the validity of a message's signature
        # The message and the signature can either be passed together, or
        # separately if the signature is decoded to raw bytes.
        # These are equivalent:
        self.public_key.verify(encoded_signature, encoder=Base64Encoder)
        self.signature_bytes = Base64Encoder.decode(encoded_signature.signature)

        return None
        
    def result(self):
        try:
            self.public_key.verify(encoded_signature.message, self.signature_bytes,
                        encoder=Base64Encoder)
            print("Signature valid")
            return True
        except:
            print("Signature was forged or corrupt")
            return False

new_verify_test = VerifierTest(verify_key_b64, encoded_signature)
print("RESULT", new_verify_test.result())