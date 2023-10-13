import time
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, padding
from cryptography.hazmat.primitives import hashes
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

# Signature Generation
rsa_signature_generation_times = []
dsa_signature_generation_times = []

for pdf_file_path in pdf_file_paths:
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()
    
    # RSA Signature Generation
    rsa_private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048
    )
    start_time = time.perf_counter()
    
    pdf_hash = hashlib.sha256(pdf_data).digest()
    signature = rsa_private_key.sign(
        pdf_hash, padding.PKCS1v15(), hashes.SHA256()
    )
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    rsa_signature_generation_times.append(execution_time)

    # DSA Signature Generation
    dsa_private_key = dsa.generate_private_key(key_size=2048)
    start_time = time.perf_counter()
    pdf_hash = hashlib.sha256(pdf_data).digest()
    signature = dsa_private_key.sign(pdf_hash, hashes.SHA256())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    dsa_signature_generation_times.append(execution_time)

# Creating the tables
signature_generation_table_data = [
    ['RSA'] + rsa_signature_generation_times,
    ['DSA'] + dsa_signature_generation_times,
]

# Improved table header names
table_headers = ['PDF Size', '10KB', '260KB', '500KB', '1MB', '10.5MB']

signature_generation_table = tabulate(signature_generation_table_data, headers=table_headers, tablefmt="grid")

# Printing the table
print("\nSignature Generation")
print(signature_generation_table)

print('done')
