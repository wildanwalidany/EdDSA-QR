import time
from ecdsa import SigningKey, SECP256k1
import nacl.signing
from tabulate import tabulate

execution_counts = [10, 50, 100, 200]

results = []

# ECDSA Signature Generation
ecdsa_times = []
for count in execution_counts:
    start_time = time.time()
    for _ in range(count):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.get_verifying_key()
        signature = sk.sign(b"message")
    end_time = time.time()
    execution_time = end_time - start_time
    ecdsa_times.append(execution_time)

results.append(ecdsa_times)

# EdDSA Signature Generation
eddsa_times = []
for count in execution_counts:
    start_time = time.time()
    for _ in range(count):
        signing_key = nacl.signing.SigningKey.generate()
        signed = signing_key.sign(b"message")
    end_time = time.time()
    execution_time = end_time - start_time
    eddsa_times.append(execution_time)

results.append(eddsa_times)

# Creating the table
table_data = []
table_data.append(['ECDSA'] + ecdsa_times)
table_data.append(['EdDSA'] + eddsa_times)

table_headers = ['Execution Count'] + execution_counts

table = tabulate(table_data, headers=table_headers, tablefmt="grid")

print(table)
