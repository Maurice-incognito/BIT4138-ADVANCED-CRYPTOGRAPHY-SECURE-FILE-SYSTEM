# Student: [Your Name] - BIT4138
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generate key and IV
key = os.urandom(32)
iv  = os.urandom(16)

# Read the file
with open("test.txt", "rb") as f:
    plaintext = f.read()

# Pad the data to be a multiple of 16 bytes
padder = padding.PKCS7(128).padder()
padded = padder.update(plaintext) + padder.finalize()

# Encrypt
cipher    = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded) + encryptor.finalize()

# Save encrypted file (IV is stored at the front so we can decrypt later)
with open("test.enc", "wb") as f:
    f.write(iv + ciphertext)

# Save key for later decryption
with open("secret.key", "wb") as f:
    f.write(key)

print("Original file  : test.txt")
print("Encrypted file : test.enc")
print("Key saved to   : secret.key")
print("File encrypted successfully!")