import time
from ecdsa import SigningKey, VerifyingKey, SECP256k1
import nacl.signing
import nacl.encoding
from tabulate import tabulate
import hashlib

# Different PDF file paths with various sizes
pdf_file_paths = [
    "dummy/100KB.pdf",
    "dummy/260KB.pdf",
    "dummy/500KB.pdf",
    "dummy/1MB.pdf",
    "dummy/10.5MB.pdf"
]

execution_count = 1  # Set execution count to 1

'========= KEY GENERATION ========='
# Key Generation
ecdsa_key_generation_times = []
eddsa_key_generation_times = []

start_time = time.perf_counter()
sk = SigningKey.generate(curve=SECP256k1)
vk = sk.get_verifying_key()
end_time = time.perf_counter()
ecdsa_key_generation_times.append(end_time - start_time)

start_time = time.perf_counter()
signing_key = nacl.signing.SigningKey.generate()
verify_key = signing_key.verify_key
end_time = time.perf_counter()
eddsa_key_generation_times.append(end_time - start_time)

'========= SIGNATURE GENERATION ========='
# Signature Generation
ecdsa_signature_generation_times = []
eddsa_signature_generation_times = []

for pdf_file_path in pdf_file_paths:
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()

    # Calculate the hash of the PDF file


    sk = SigningKey.generate(curve=SECP256k1)

    start_time = time.perf_counter()
    pdf_hash = hashlib.sha256(pdf_data).digest()
    signature = sk.sign(pdf_hash)
    end_time = time.perf_counter()
    ecdsa_signature_generation_times.append(end_time - start_time)

    signing_key = nacl.signing.SigningKey.generate()

    start_time = time.perf_counter()
    pdf_hash = hashlib.sha256(pdf_data).digest()
    signed = signing_key.sign(pdf_hash)
    end_time = time.perf_counter()
    eddsa_signature_generation_times.append(end_time - start_time)

'========= SIGNATURE VERIFICATION ========='
ecdsa_signature_verification_times = []
eddsa_signature_verification_times = []

for pdf_file_path in pdf_file_paths:
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()

    # Calculate the hash of the PDF file


    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()
    
    start_time = time.perf_counter()

    pdf_hash = hashlib.sha256(pdf_data).digest()
    signature = sk.sign(pdf_hash)


    vk.verify(signature, pdf_hash)
    end_time = time.perf_counter()
    ecdsa_signature_verification_times.append(end_time - start_time)

    signing_key = nacl.signing.SigningKey.generate()
    
    
    start_time = time.perf_counter()   
    verify_key = signing_key.verify_key
    pdf_hash = hashlib.sha256(pdf_data).digest()
    signed = signing_key.sign(pdf_hash)


    verify_key.verify(signed.message, signed.signature)
    end_time = time.perf_counter()
    eddsa_signature_verification_times.append(end_time - start_time)

# Improved table header names
table_headers = ['PDF Size', '10KB', '260KB', '500KB', '1MB', '10.5MB']

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
