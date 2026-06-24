# Student: [Your Name] - BIT4138
from collections import Counter

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

plaintext  = "CRYPTOGRAPHY IS THE SCIENCE OF SECURE COMMUNICATION AND DATA PROTECTION"
shift      = 13
ciphertext = caesar_encrypt(plaintext, shift)

print("=== Frequency Analysis Tool ===")
print()
print(f"Ciphertext: {ciphertext}")
print()

# Count letter frequencies in ciphertext
letters    = [c for c in ciphertext if c.isalpha()]
freq       = Counter(letters)
total      = len(letters)

print(f"{'Letter':<10} {'Count':<10} {'Frequency %':<15} {'Bar'}")
print("-" * 55)

for letter, count in sorted(freq.items(), key=lambda x: -x[1]):
    pct = (count / total) * 100
    bar = "█" * int(pct)
    print(f"{letter:<10} {count:<10} {pct:<15.1f} {bar}")

print()
print("=== Statistical Insight ===")
most_common = freq.most_common(1)[0]
print(f"Most frequent letter: {most_common[0]} ({most_common[1]} times)")
print("In English, E is most common — if cipher is Caesar, most frequent = E")
likely_shift = ord(most_common[0]) - ord('E')
print(f"Likely shift value   : {likely_shift % 26}")
print("Frequency analysis reveals the key without brute force!")