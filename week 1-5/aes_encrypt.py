# Student: [Your Name] - BIT4138

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# ── Step 1: Generate a 256-bit AES key and a 16-byte IV ──
key = os.urandom(32)   # 32 bytes = 256 bits
iv  = os.urandom(16)   # 16 bytes = 128-bit IV (required for CBC mode)

print("=== AES-256-CBC Encryption ===")
print(f"Key (hex) : {key.hex()}")
print(f"IV  (hex) : {iv.hex()}")

# ── Step 2: Define the plaintext message ──
plaintext = b"Hello BIT4138! This is a secure message using AES-256."
print(f"\nPlaintext : {plaintext.decode()}")

# ── Step 3: Pad the plaintext to a multiple of 16 bytes ──
# AES requires input length to be a multiple of 16 (block size)
padder        = padding.PKCS7(128).padder()
padded_data   = padder.update(plaintext) + padder.finalize()

# ── Step 4: Create the AES cipher and encrypt ──
cipher        = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor     = cipher.encryptor()
ciphertext    = encryptor.update(padded_data) + encryptor.finalize()

print(f"Ciphertext (hex): {ciphertext.hex()}")
print(f"\nOriginal length  : {len(plaintext)} bytes")
print(f"Encrypted length : {len(ciphertext)} bytes")
print("\nEncryption successful!")