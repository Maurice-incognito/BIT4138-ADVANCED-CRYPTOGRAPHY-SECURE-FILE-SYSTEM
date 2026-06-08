# Student: [Your Name] - BIT4138

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

print("=== RSA Public Key Encryption ===")
print()

# ── Load the public key from file ──
with open("keys/public.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

print("Public key loaded from: keys/public.pem")

# ── Define the message to encrypt ──
message = b"This is a confidential message for BIT4138 Cryptography."
print(f"Original message : {message.decode()}")
print(f"Message length   : {len(message)} bytes")
print()

# ── Encrypt the message using the public key ──
# OAEP padding is the secure modern standard for RSA encryption
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# ── Save the encrypted message to a file ──
with open("encrypted_msg.bin", "wb") as f:
    f.write(ciphertext)

print(f"Encrypted (hex)  : {ciphertext.hex()[:80]}...")
print(f"Encrypted length : {len(ciphertext)} bytes")
print()
print("Encrypted message saved to: encrypted_msg.bin")
print()
print("Encryption successful!")
print("Only the holder of private.pem can decrypt this message.")