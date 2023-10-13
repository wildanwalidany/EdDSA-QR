import time
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, padding
from cryptography.hazmat.primitives import hashes
from tabulate import tabulate

execution_counts = [10, 50, 100, 200, 500]

# Key Generation
rsa_key_generation_times = []
dsa_key_generation_times = []

for count in execution_counts:
    # RSA Key Generation
    start_time = time.perf_counter()
    for _ in range(count):
        rsa_private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048
        )
        rsa_public_key = rsa_private_key.public_key()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    rsa_key_generation_times.append(execution_time)
    
    # DSA Key Generation
    start_time = time.perf_counter()
    for _ in range(count):
        dsa_private_key = dsa.generate_private_key(key_size=2048)
        dsa_public_key = dsa_private_key.public_key()
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    dsa_key_generation_times.append(execution_time)

# Creating the tables
key_generation_table_data = [
    ['RSA'] + rsa_key_generation_times,
    ['DSA'] + dsa_key_generation_times,
]
table_headers = ['Execution Count'] + execution_counts
key_generation_table = tabulate(key_generation_table_data, headers=table_headers, tablefmt="grid")
# Printing the tables
print("Key Generation")
print(key_generation_table)


print('done')