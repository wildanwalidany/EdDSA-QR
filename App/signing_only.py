from json_generator import JsonGen
from qr_encoder import QREncode
from sign_generator import SignGenerator
from user import User


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
    new_json = JsonGen(name, 'pengesahan proposal PA', 'jane foster')
    identity = new_json.to_json_bytes()
    print('IDENTITY', identity)
    
    '============= SIGNING ============='
    # Create new sign object
    new_sign = SignGenerator(private_key, identity)
    signed_message = new_sign.get_signed()

    print('message',signed_message.message)
    print('len',len(signed_message.message))
    print('signature',signed_message.signature)
    print('len',len(signed_message.signature))
    print('SIGNED MESSAGE', signed_message)
    print('len', len(signed_message))
    
    '============= ENCODE =============' 
    new_qr = QREncode(signed_message)

    print("jalan coy ✅✅✅")
    
if __name__ == "__main__":
    main()
