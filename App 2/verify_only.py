from sign_generator import SignGenerator
from verifier import Verifier
from user import User
from json_generator import JsonGEn
from qr_reader import Reader
from nacl.encoding import Base64Encoder
import nacl.signing

def main():

    '============= VERIFY ============='
    # Read QR Code
    new_read = Reader()
    data = new_read.read()

    signed_bytes = Base64Encoder.decode(data)
    signed_message = signed_bytes.split(b'{')
    print(signed_bytes)
    # Find(identity)
    
    # Get(public_key)
    
    
    # Create new verify object
    '''
    new_verify = Verifier(public_key, signature)
    result = new_verify.result()
    print('RESULT', result)
    '''



    print("jalan coy")
    
if __name__ == "__main__":
    main()
