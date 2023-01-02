from sign_generator import SignGenerator
from verifier import Verifier
from user import User
from json_generator import JsonGEn
from qr_reader import Reader
from nacl.encoding import Base64Encoder
import json
from key_finder import Finder

def main():

    '============= VERIFY ============='
    # Read QR Code
    new_read = Reader()
    data = new_read.read()

    # Decode the signed message
    signed_bytes = Base64Encoder.decode(data)


    # Extract the message
    word = b'{"name"'
    start_index = signed_bytes.index(word)
    rest_of_bytes = signed_bytes[start_index:]
    print(rest_of_bytes)  
    
    # Parse the string as a JSON object
    json_obj = json.loads(rest_of_bytes)

    # Access the "name" field
    name = json_obj["name"]

    print(name) 

    # Find(identity)
    new_find = Finder(name)

    # Get(public_key)
    public_key = new_find.find()
    print(public_key)

    # Create new verify object
    
    new_verify = Verifier(public_key, data)
    result = new_verify.result()
    print('RESULT', result)

    print("ᨐᵉᵒʷ")
    
if __name__ == "__main__":
    main()
