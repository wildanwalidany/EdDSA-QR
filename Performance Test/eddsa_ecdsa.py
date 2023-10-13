import time
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import nacl.signing
import nacl.encoding
from tabulate import tabulate

execution_counts = [10, 50, 100, 200, 500]

'========= KEY GENERATION ========='
# Key Generation
ecdsa_key_generation_times = []
eddsa_key_generation_times = []

for count in execution_counts:
    start_time = time.perf_counter()
    for _ in range(count):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.get_verifying_key()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    ecdsa_key_generation_times.append(execution_time)

    start_time = time.perf_counter()
    for _ in range(count):
        signing_key = nacl.signing.SigningKey.generate()
        verify_key = signing_key.verify_key
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    eddsa_key_generation_times.append(execution_time)

'========= SIGNATURE GENERATION ========='
# Signature Generation
ecdsa_signature_generation_times = []
eddsa_signature_generation_times = []

for count in execution_counts:
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()

    start_time = time.perf_counter()
    for _ in range(count):
        signature = sk.sign(b"message")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    ecdsa_signature_generation_times.append(execution_time)

    signing_key = nacl.signing.SigningKey.generate()
    verify_key = signing_key.verify_key

    start_time = time.perf_counter()
    for _ in range(count):
        signed = signing_key.sign(b"message")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    eddsa_signature_generation_times.append(execution_time)

'========= SIGNATURE VERIFICATION GENERATION ========='
ecdsa_signature_verification_times = []
eddsa_signature_verification_times = []

for count in execution_counts:
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()
    signature = sk.sign(b"message")

    start_time = time.perf_counter()
    for _ in range(count):
        vk.verify(signature, b"message")
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    ecdsa_signature_verification_times.append(execution_time)

    signing_key = nacl.signing.SigningKey.generate()
    verify_key = signing_key.verify_key
    signed = signing_key.sign(b"message")

    start_time = time.perf_counter()
    for _ in range(count):
        verify_key.verify(signed.message, signed.signature)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    eddsa_signature_verification_times.append(execution_time)

# Creating the tables
key_generation_table_data = [
    ['EdDSA'] + eddsa_key_generation_times,
    ['ECDSA'] + ecdsa_key_generation_times    
]

signature_generation_table_data = [
    ['EdDSA'] + eddsa_signature_generation_times,
    ['ECDSA'] + ecdsa_signature_generation_times
]

signature_verification_table_data = [
    ['EdDSA'] + eddsa_signature_verification_times,
    ['ECDSA'] + ecdsa_signature_verification_times

]

table_headers = ['Execution Count'] + execution_counts

key_generation_table = tabulate(key_generation_table_data, headers=table_headers, tablefmt="grid")
signature_generation_table = tabulate(signature_generation_table_data, headers=table_headers, tablefmt="grid")
signature_verification_table = tabulate(signature_verification_table_data, headers=table_headers, tablefmt="grid")

# Printing the tables
print("Key Generation")
print(key_generation_table)
print("\nSignature Generation")
print(signature_generation_table)
print("\nSignature Verification")
print(signature_verification_table)
