# Student: [Your Name] - BIT4138

# S-Box: maps each input value to a substituted output value
sbox = {
    0: 14,  1: 4,   2: 13,  3: 1,
    4: 2,   5: 15,  6: 11,  7: 8,
    8: 3,   9: 10,  10: 6,  11: 12,
    12: 5,  13: 9,  14: 0,  15: 7
}

# Inverse S-Box for decryption
inv_sbox = {v: k for k, v in sbox.items()}

print("=== S-Box Substitution Table ===")
print()
print(f"{'Input':<10} {'Output':<10} {'Binary In':<15} {'Binary Out'}")
print("-" * 50)

for i in range(16):
    output = sbox[i]
    print(f"{i:<10} {output:<10} {bin(i)[2:].zfill(4):<15} {bin(output)[2:].zfill(4)}")

print()
print("=== Test Substitutions ===")
test_inputs = [0, 2, 5, 9, 12]
for val in test_inputs:
    print(f"S-Box({val}) = {sbox[val]}")

print()
print("S-Box applied successfully!")
print(f"Total mappings: {len(sbox)}")
print("All output values unique:", len(set(sbox.values())) == len(sbox))