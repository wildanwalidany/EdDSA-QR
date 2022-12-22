from sign_generator import SignGenerator
from verifier import Verifier
from user import User
from json_generator import JsonGEn

def main():

    '============= VERIFY ============='
    # GET identity + ignature
    # Find(identity)
    # Get(public_key)

    # Create new verify object
    new_verify = Verifier(public_key, signature)
    result = new_verify.result()
    print('RESULT', result)




    print("jalan coy")
    
if __name__ == "__main__":
    main()
