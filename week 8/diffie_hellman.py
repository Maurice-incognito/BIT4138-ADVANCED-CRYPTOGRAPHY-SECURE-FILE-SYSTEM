# Student: [Your Name] - BIT4138

print("=== Diffie-Hellman Key Exchange ===")
print()

# Public parameters (both parties know these)
p = 23   # prime number
g = 5    # generator

print(f"Public Parameters:")
print(f"  Prime (p)     : {p}")
print(f"  Generator (g) : {g}")
print()

# Private keys (each party keeps secret)
alice_private = 6
bob_private   = 15

print(f"Private Keys (secret):")
print(f"  Alice private : {alice_private}")
print(f"  Bob private   : {bob_private}")
print()

# Generate public keys
alice_public = (g ** alice_private) % p
bob_public   = (g ** bob_private) % p

print(f"Public Keys (exchanged openly):")
print(f"  Alice public  : g^a mod p = {g}^{alice_private} mod {p} = {alice_public}")
print(f"  Bob public    : g^b mod p = {g}^{bob_private} mod {p} = {bob_public}")
print()

# Compute shared secret
alice_secret = (bob_public ** alice_private) % p
bob_secret   = (alice_public ** bob_private) % p

print(f"Shared Secret Computation:")
print(f"  Alice computes: B^a mod p = {bob_public}^{alice_private} mod {p} = {alice_secret}")
print(f"  Bob computes  : A^b mod p = {alice_public}^{bob_private} mod {p} = {bob_secret}")
print()

if alice_secret == bob_secret:
    print(f"Shared Secret : {alice_secret}")
    print()
    print("Key exchange SUCCESSFUL!")
    print("Both parties now share the same secret without ever transmitting it.")
else:
    print("Error: Secrets do not match.")