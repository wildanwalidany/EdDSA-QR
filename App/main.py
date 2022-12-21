from sign_generator import SignGenerator
from verifier import Verifier
from user import User


def main():
    
    new_acc = User("grizzly", "pass_grizzly")
    # new_acc.sign_up()

    private_key, public_key = new_acc.login()
    print(private_key, public_key)

    # Define Message
    message = b'Wildan Dharma Walidaniy'
    
    '============= SIGNING ============='
    # Create new sign object
    new_sign = SignGenerator(private_key, message)
    signature = new_sign.get_signature()

    print('SIGNATURE', signature)

    '============= VERIFY ============='
    # Create new verify object
    new_verify = Verifier(public_key, signature)
    result = new_verify.result()
    print('RESULT', result)




    print("jalan coy")
    
if __name__ == "__main__":
    main()
