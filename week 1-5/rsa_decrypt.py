# Student: [Your Name] - BIT4138
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# ── Load the private key from the keys folder ──
with open("keys/private.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)

# ── Load the encrypted message ──
with open("encrypted_msg.bin", "rb") as f:
    ciphertext = f.read()

# ── Decrypt using the private key ──
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("=== RSA Private Key Decryption ===")
print()
print("Decrypted message:", plaintext.decode())
print()
print("Decryption successful!")