from nacl.encoding import Base64Encoder
from nacl.signing import VerifyKey

class Verifier():
    def __init__(self, public_key_b64, signed_b64):
        self.encoded_signed = signed_b64
        # Create a VerifyKey object from a base64 serialized public key
        self.public_key = VerifyKey(public_key_b64, encoder=Base64Encoder)

        return None

    def result(self):
        try:
            # Check the validity of a message's signature
            self.public_key.verify(self.encoded_signed, encoder=Base64Encoder)
            print("Signature valid")
            return True
        except:
            print("Signature was forged or corrupt")
            return False