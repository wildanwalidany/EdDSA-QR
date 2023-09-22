import time
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def generate_ecdsa_signature(private_key, message):
    start_time = time.time()
    signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))
    end_time = time.time()
    return end_time - start_time

# Execution counts
execution_counts = [10, 50, 100, 200]

# Key sizes
ecdsa_key_sizes = [256, 384, 521]

# Table header
print("Execution count\tKey Size\tExecution time")

# Calculate execution time for each count and key size
for count in execution_counts:
    for key_size in ecdsa_key_sizes:
        # Generate ECDSA key pair
        curve = ec.SECP256R1() if key_size == 256 else ec.SECP384R1() if key_size == 384 else ec.SECP521R1()
        private_key = ec.generate_private_key(curve, default_backend())

        # Message to be signed
        message = b"Hello, world!"
        
        total_time = 0.0
        for _ in range(count):
            execution_time = generate_ecdsa_signature(private_key, message)
            total_time += execution_time
        
        average_time = total_time / count
        print(f"{count}\t\t{key_size}\t\t{total_time:.6f} seconds")
