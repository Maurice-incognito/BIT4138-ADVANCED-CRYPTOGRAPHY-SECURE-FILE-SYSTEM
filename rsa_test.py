# Student: [Your Name] - BIT4138
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

print("Running RSA unit tests...")

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key  = private_key.public_key()

test_messages = [b"Hello", b"BIT4138 Test", b"Cryptography Works!"]

for msg in test_messages:
    encrypted = public_key.encrypt(msg,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None))
    decrypted = private_key.decrypt(encrypted,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                     algorithm=hashes.SHA256(), label=None))
    assert decrypted == msg, f"FAILED for: {msg}"
    print(f"  Test '{msg.decode()}' => PASS")

print("\nAll tests passed! RSA encryption and decryption working correctly.")