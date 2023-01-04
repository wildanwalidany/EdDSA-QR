import json

from key_finder import Finder
from nacl.encoding import Base64Encoder
from qr_reader import Reader
from verifier import Verifier


def main():

    '============= VERIFY ============='
    # Read QR Code
    new_read = Reader()
    data = new_read.read()
    print('data read', data)

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

    print('name', name) 

    # Find(identity)
    new_find = Finder(name)

    # Get(public_key)
    public_key = new_find.find()
    print('public_key', public_key)

    # Create new verify object
    
    new_verify = Verifier(public_key, data)
    result = new_verify.result()
    print('RESULT', result)

    print("✅✅✅")
    
if __name__ == "__main__":
    main()
