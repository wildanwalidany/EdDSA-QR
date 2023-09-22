from sign_generator import SignGenerator
from verifier import Verifier
from user import User
from json_generator import JsonGEn

def main():
    '============= Sign Up, Login ============='
    # Create new user object
    new_acc = User("grizzly", "pass_grizzly")
    # new_acc.sign_up()

    private_key, public_key = new_acc.login()
    print("PRIVATE", private_key, "PUBLIC", public_key)

    '============= Identity ============='
    # Create an object
    new_json = JsonGEn(new_acc.username, "Mjollnir", "Jane Foster")

    # get the json object in bytes
    identity = new_json.to_json_bytes()


    '============= SIGNING ============='
    # Create new sign object
    new_sign = SignGenerator(private_key, identity)
    signature = new_sign.get_signature()

    print('SIGNATURE', signature)

    '============= ENCODE =============' 
       





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
