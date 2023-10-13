import time
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, padding
from cryptography.hazmat.primitives import hashes
from tabulate import tabulate

execution_counts = [10, 50, 100, 200, 500]

# Signature Generation
rsa_signature_generation_times = []
dsa_signature_generation_times = []

for count in execution_counts:
    # RSA Signature Generation
    rsa_private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048
    )
    start_time = time.perf_counter()
    for _ in range(count):
        signature = rsa_private_key.sign(
            b"message", padding.PKCS1v15(), hashes.SHA256()
        )
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    rsa_signature_generation_times.append(execution_time)

    # DSA Signature Generation
    dsa_private_key = dsa.generate_private_key(key_size=2048)
    start_time = time.perf_counter()
    for _ in range(count):
        signature = dsa_private_key.sign(b"message", hashes.SHA256())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    dsa_signature_generation_times.append(execution_time)


# Creating the tables
signature_generation_table_data = [
    ['RSA'] + rsa_signature_generation_times,
    ['DSA'] + dsa_signature_generation_times,
]
table_headers = ['Execution Count'] + execution_counts
signature_generation_table = tabulate(signature_generation_table_data, headers=table_headers, tablefmt="grid")

# Printing the tables
print("\nSignature Generation")
print(signature_generation_table)

print('done')