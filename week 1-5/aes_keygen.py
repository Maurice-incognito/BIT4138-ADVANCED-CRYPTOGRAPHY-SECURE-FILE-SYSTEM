# Student: [Your Name] - BIT4138

import os

print("=== AES-256 Key Generation ===")
print()

# Generate a secure 256-bit key using os.urandom
# os.urandom uses the operating system's secure random number generator
key = os.urandom(32)   # 32 bytes = 256 bits
iv  = os.urandom(16)   # 16 bytes IV for CBC mode

print(f"Key size     : {len(key) * 8} bits ({len(key)} bytes)")
print(f"Key (hex)    : {key.hex()}")
print()
print(f"IV size      : {len(iv) * 8} bits ({len(iv)} bytes)")
print(f"IV  (hex)    : {iv.hex()}")
print()

# Save the key to a file in the /keys folder
os.makedirs("keys", exist_ok=True)   # create keys/ folder if it doesn't exist

with open("keys/aes_key.bin", "wb") as f:
    f.write(key)

with open("keys/aes_iv.bin", "wb") as f:
    f.write(iv)

print("Key saved to : keys/aes_key.bin")
print("IV  saved to : keys/aes_iv.bin")
print()
print("Key generation complete!")
print("IMPORTANT: Never share your key file with anyone.")