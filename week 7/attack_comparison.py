# Student: [Your Name] - BIT4138

print("=== Block Cipher Attack Comparison Report ===")
print()

attacks = [
    {
        "name": "Brute Force Attack",
        "type": "Exhaustive Search",
        "speed": "Very Slow",
        "complexity": "O(2^n) — exponential",
        "data_needed": "One plaintext-ciphertext pair",
        "success_rate": "100% (given enough time)",
        "practical": "No — infeasible for AES-256"
    },
    {
        "name": "Algebraic Attack",
        "type": "Mathematical",
        "speed": "Fast on weak ciphers",
        "complexity": "Polynomial on linear ciphers",
        "data_needed": "Known plaintext-ciphertext pairs",
        "success_rate": "High on weak S-Boxes",
        "practical": "Only against poorly designed ciphers"
    },
    {
        "name": "Differential Cryptanalysis",
        "type": "Chosen Plaintext",
        "speed": "Moderate",
        "complexity": "Depends on cipher rounds",
        "data_needed": "Many chosen plaintext pairs",
        "success_rate": "High against weak ciphers",
        "practical": "Defeated by strong S-Boxes and diffusion"
    },
    {
        "name": "Linear Cryptanalysis",
        "type": "Known Plaintext",
        "speed": "Moderate",
        "complexity": "Statistical — needs large data",
        "data_needed": "Large amounts of plaintext-ciphertext",
        "success_rate": "Depends on linear bias",
        "practical": "Defeated by high non-linearity"
    }
]

for a in attacks:
    print(f"{'='*55}")
    print(f"  Attack          : {a['name']}")
    print(f"  Type            : {a['type']}")
    print(f"  Speed           : {a['speed']}")
    print(f"  Complexity      : {a['complexity']}")
    print(f"  Data Needed     : {a['data_needed']}")
    print(f"  Success Rate    : {a['success_rate']}")
    print(f"  Practical Today : {a['practical']}")
    print()

print("=== Conclusion ===")
print("AES-256 is resistant to all four attack types.")
print("Strong S-Boxes, multiple rounds, and high diffusion")
print("make modern block ciphers practically unbreakable.")