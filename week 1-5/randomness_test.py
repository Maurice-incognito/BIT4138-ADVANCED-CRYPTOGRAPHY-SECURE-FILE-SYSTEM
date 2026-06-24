# Student: [Your Name] - BIT4138

import random

# Generate 100 random bits
bits = [random.randint(0, 1) for _ in range(100)]
print("Generated bits:", bits[:20], "... (100 total)")

# Frequency Test - count how many 0s and 1s
zeros = bits.count(0)
ones  = bits.count(1)
print("\n--- Frequency Test ---")
print(f"Zeros: {zeros}  |  Ones: {ones}")
if 40 <= ones <= 60:
    print("Result: PASS (good balance between 0s and 1s)")
else:
    print("Result: FAIL (too many 0s or 1s)")

# Runs Test - count how many times the bit changes
runs = 1
for i in range(1, len(bits)):
    if bits[i] != bits[i-1]:
        runs += 1
print("\n--- Runs Test ---")
print(f"Number of runs: {runs}")
if 40 <= runs <= 75:
    print("Result: PASS (bits change frequently enough)")
else:
    print("Result: FAIL")

# Chi-Square quick check
print("\n--- Chi-Square Test ---")
expected = 50
chi = ((zeros - expected)**2 / expected) + ((ones - expected)**2 / expected)
print(f"Chi-Square value: {chi:.4f}")
if chi < 3.841:
    print("Result: PASS (distribution looks random)")
else:
    print("Result: FAIL")