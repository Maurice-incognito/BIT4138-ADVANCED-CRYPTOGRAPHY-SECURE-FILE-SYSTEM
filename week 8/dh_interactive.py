# Student: [Your Name] - BIT4138

print("=== Interactive Diffie-Hellman Key Exchange ===")
print()

# Get public parameters from user
p = int(input("Enter a prime number (p) [try 23]: "))
g = int(input("Enter a generator (g)    [try 5] : "))
print()

# Get private keys
alice_private = int(input("Enter Alice's private key [try 6] : "))
bob_private   = int(input("Enter Bob's private key   [try 15]: "))
print()

# Compute public keys
alice_public = (g ** alice_private) % p
bob_public   = (g ** bob_private)   % p

print(f"--- Generated Public Keys ---")
print(f"Alice's public key : {alice_public}")
print(f"Bob's public key   : {bob_public}")
print()

# Compute shared secrets
alice_secret = (bob_public  ** alice_private) % p
bob_secret   = (alice_public ** bob_private)  % p

print(f"--- Shared Secret ---")
print(f"Alice computed : {alice_secret}")
print(f"Bob computed   : {bob_secret}")
print()

if alice_secret == bob_secret:
    print(f"Shared Secret Key  : {alice_secret}")
    print("Verification       : PASSED")
    print()
    print("Both users independently arrived at the same secret.")
    print("An eavesdropper only sees p, g, A, and B — not the secret!")
else:
    print("Verification FAILED — check your inputs.")