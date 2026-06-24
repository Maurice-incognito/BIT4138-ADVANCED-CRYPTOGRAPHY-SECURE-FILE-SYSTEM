# Student: [Your Name] - BIT4138

print("=== XOR Algebraic Attack Simulation ===")
print()
print("Scenario: Simple XOR cipher C = P XOR K")
print("Attacker knows plaintext P and ciphertext C")
print("Goal: Recover secret key K")
print()

# Simulate encryption
secret_key = 0b10110101  # attacker does NOT know this
plaintext  = 0b11001010  # attacker knows this

ciphertext = plaintext ^ secret_key  # attacker observes this

print(f"Known Plaintext  (P): {bin(plaintext)}  = {plaintext}")
print(f"Observed Ciphertext (C): {bin(ciphertext)} = {ciphertext}")
print()

# Algebraic attack: K = P XOR C
recovered_key = plaintext ^ ciphertext

print("=== Applying Algebraic Attack ===")
print(f"K = P XOR C")
print(f"K = {bin(plaintext)} XOR {bin(ciphertext)}")
print(f"Recovered Key: {bin(recovered_key)} = {recovered_key}")
print()

if recovered_key == secret_key:
    print("Attack SUCCESSFUL — Key recovered!")
else:
    print("Attack failed.")

print()
print("=== Why This Works ===")
print("XOR is a linear operation.")
print("Linear ciphers are vulnerable to algebraic attacks.")
print("This is why modern ciphers use non-linear S-Boxes.")
