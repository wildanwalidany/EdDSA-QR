import time
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def generate_ed25519_signature(private_key, message):
    start_time = time.time()
    signature = private_key.sign(message)
    end_time = time.time()
    return end_time - start_time

# Execution counts
execution_counts = [10, 50, 100, 200]

# Generate Ed25519 key pair
private_key = ed25519.Ed25519PrivateKey.generate()

# Message to be signed
message = b"Hello, world!"

# Table header
print("Execution count\tExecution time")

# Calculate execution time for each count
for count in execution_counts:
    total_time = 0.0
    for _ in range(count):
        execution_time = generate_ed25519_signature(private_key, message)
        total_time += execution_time
    
    average_time = total_time / count
    print(f"{count}\t\t{total_time:.6f} seconds")
