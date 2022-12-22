from sign_generator import SignGenerator
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
    print('IDENTITY', identity)

    '============= SIGNING ============='
    # Create new sign object
    new_sign = SignGenerator(private_key, identity)
    signature = new_sign.get_signature()

    print('SIGNATURE', signature)
    print('size in bytes', len(signature))

    
    '============= ENCODE =============' 


    print("jalan coy")
    
if __name__ == "__main__":
    main()
