# Student: [Your Name] - BIT4138
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Load the key
with open("secret.key", "rb") as f:
    key = f.read()

# Load the encrypted file
with open("test.enc", "rb") as f:
    data = f.read()

# First 16 bytes are the IV, rest is ciphertext
iv         = data[:16]
ciphertext = data[16:]

# Decrypt
cipher    = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()
padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Remove padding
unpadder   = padding.PKCS7(128).unpadder()
plaintext  = unpadder.update(padded_plaintext) + unpadder.finalize()

# Save recovered file
with open("test_recovered.txt", "wb") as f:
    f.write(plaintext)

print("Decrypted content:")
print(plaintext.decode())
print("File saved as: test_recovered.txt")