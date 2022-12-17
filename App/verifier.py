from nacl.encoding import Base64Encoder
from nacl.signing import VerifyKey

class Verifier():
    def __init__(self, public_key_b64, encoded_signature):
        self.encoded_signature = encoded_signature
        # Create a VerifyKey object from a base64 serialized public key
        self.public_key = VerifyKey(public_key_b64, encoder=Base64Encoder)

        # Check the validity of a message's signature
        self.public_key.verify(encoded_signature, encoder=Base64Encoder)
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