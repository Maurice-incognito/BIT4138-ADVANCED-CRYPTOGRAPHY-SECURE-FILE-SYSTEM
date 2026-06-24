# Student: [Your Name] - BIT4138
import hashlib

def count_bit_differences(val1, val2, bits=256):
    xor = val1 ^ val2
    return bin(xor).count('1')

def sha256_int(text):
    h = hashlib.sha256(text.encode()).hexdigest()
    return int(h, 16)

pairs = [
    ("HELLO", "HELLo"),
    ("BIT4138", "BIT4139"),
    ("cryptography", "Cryptography"),
    ("secure", "securd"),
]

print("=== Avalanche Effect Demonstration ===")
print()
print(f"{'Input 1':<20} {'Input 2':<20} {'Bits Changed':<15} {'Avalanche %'}")
print("-" * 70)

for t1, t2 in pairs:
    h1   = sha256_int(t1)
    h2   = sha256_int(t2)
    diff = count_bit_differences(h1, h2)
    pct  = (diff / 256) * 100
    print(f"{t1:<20} {t2:<20} {diff:<15} {pct:.1f}%")

print()
print("=== Detailed Example ===")
text1 = "HELLO"
text2 = "HELLo"
h1 = hashlib.sha256(text1.encode()).hexdigest()
h2 = hashlib.sha256(text2.encode()).hexdigest()
print(f"Input 1 : {text1}")
print(f"Input 2 : {text2}")
print(f"Hash 1  : {h1}")
print(f"Hash 2  : {h2}")
print()
print("Only ONE character changed — but the hashes are completely different!")
print("This is the Avalanche Effect.")