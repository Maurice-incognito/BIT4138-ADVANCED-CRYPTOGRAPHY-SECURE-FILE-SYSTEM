# Student: [Your Name] - BIT4138
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as sym_padding
import os, time

def encrypt_data(data, key, iv):
    padder = sym_padding.PKCS7(128).padder()
    padded = padder.update(data) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    enc = cipher.encryptor()
    return enc.update(padded) + enc.finalize()

key = os.urandom(32)
iv  = os.urandom(16)

sizes = {"1 KB": 1024, "10 KB": 10240, "1 MB": 1048576}

print("=== AES-256 Encryption Performance ===")
print(f"{'File Size':<12} {'Time (ms)':<15} {'Speed'}")
print("-" * 45)

for label, size in sizes.items():
    data  = os.urandom(size)
    start = time.time()
    encrypt_data(data, key, iv)
    elapsed = (time.time() - start) * 1000
    speed = size / (elapsed / 1000) / 1024
    print(f"{label:<12} {elapsed:<15.4f} {speed:.1f} KB/s")