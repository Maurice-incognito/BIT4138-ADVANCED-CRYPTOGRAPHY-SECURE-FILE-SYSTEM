# Student: [Your Name] - BIT4138

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

print("=== RSA Key Pair Generation ===")
print()
print("Generating 2048-bit RSA key pair...")
print("(This may take a moment...)")
print()

# Generate the private key
private_key = rsa.generate_private_key(
    public_exponent=65537,   # standard public exponent used in RSA
    key_size=2048            # 2048-bit key = industry standard minimum
)

# Derive the public key from the private key
public_key = private_key.public_key()

# ── Save private key as private.pem ──
os.makedirs("keys", exist_ok=True)

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
with open("keys/private.pem", "wb") as f:
    f.write(private_pem)

# ── Save public key as public.pem ──
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open("keys/public.pem", "wb") as f:
    f.write(public_pem)

# ── Display summary ──
print(f"Key type     : RSA")
print(f"Key size     : 2048 bits")
print(f"Public exp   : 65537")
print()
print("Private key saved to : keys/private.pem")
print("Public  key saved to : keys/public.pem")
print()
print("First 3 lines of public key:")
for line in public_pem.decode().split("\n")[:3]:
    print(" ", line)
print()
print("Key generation successful!")
print("Share public.pem freely. Keep private.pem SECRET.")