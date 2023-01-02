from sign_generator import SignGenerator
from user import User
from json_generator import JsonGEn
from qr_encoder import QREncode

def main():
    '============= Sign Up, Login ============='
    # Create new user object
    name = "grizzly"
    pswd = "pass_grizzly"
    new_acc = User(name, pswd)
    # new_acc.sign_up()

    private_key, public_key = new_acc.login()
    print("PRIVATE", private_key, "PUBLIC", public_key)

    '============= Identity ============='
    new_json = JsonGEn(name, 'pengesahan proposal PA', 'jane foster')
    identity = new_json.to_json_bytes()
    print('IDENTITY', identity)
    
    '============= SIGNING ============='
    # Create new sign object
    new_sign = SignGenerator(private_key, identity)
    signed_message = new_sign.get_signature()

    print('message',signed_message.message)
    print('len',len(signed_message.message))
    print('signature',signed_message.signature)
    print('len',len(signed_message.signature))
    print('SIGNED MESSAGE', signed_message)
    print('len', len(signed_message))
    
    '============= ENCODE =============' 
    new_qr = QREncode(signed_message)

    print("jalan coy")
    
if __name__ == "__main__":
    main()
