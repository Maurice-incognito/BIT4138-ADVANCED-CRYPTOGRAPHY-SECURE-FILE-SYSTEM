# Student: [Your Name] - BIT4138

def permute(bits, permutation_table):
    """
    Rearranges bits according to the permutation table.
    permutation_table[i] tells us which original position
    goes to position i in the output.
    """
    return [bits[permutation_table[i]] for i in range(len(permutation_table))]

# 16-bit permutation table (defines new positions)
P_TABLE = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]

# Example 16-bit input
plaintext_bits = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1]

print("=== Permutation Operation ===")
print()
print(f"Original bits  : {plaintext_bits}")
print(f"Permutation table: {P_TABLE}")
print()

permuted = permute(plaintext_bits, P_TABLE)

print(f"Permuted bits  : {permuted}")
print()

# Show how bits moved
print("=== Bit Movement Trace ===")
for i, p in enumerate(P_TABLE[:8]):
    print(f"  Position {p} -> Position {i}  |  Bit value: {plaintext_bits[p]}")

print()
print("Permutation complete!")
print("Original :", ''.join(str(b) for b in plaintext_bits))
print("Permuted :", ''.join(str(b) for b in permuted))