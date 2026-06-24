# Student: [Your Name] - BIT4138

sbox = {
    0:14, 1:4,  2:13, 3:1,
    4:2,  5:15, 6:11, 7:8,
    8:3,  9:10, 10:6, 11:12,
    12:5, 13:9, 14:0, 15:7
}

def simple_encrypt(plaintext, key):
    return sbox[(plaintext ^ key) % 16]

print("=== Differential Cryptanalysis Simulation ===")
print()
print("Concept: Study how input differences affect output differences")
print()

key = 7  # secret key (attacker tries to discover this)

# Generate pairs with fixed input difference
input_diff = 0b0001  # difference of 1 between inputs

print(f"Fixed input difference: {bin(input_diff)} ({input_diff})")
print()
print(f"{'P1':<6} {'P2':<6} {'C1':<6} {'C2':<6} {'Input XOR':<12} {'Output XOR'}")
print("-" * 55)

output_diffs = {}
for p1 in range(8):
    p2   = p1 ^ input_diff
    c1   = simple_encrypt(p1, key)
    c2   = simple_encrypt(p2, key)
    idiff = p1 ^ p2
    odiff = c1 ^ c2
    print(f"{p1:<6} {p2:<6} {c1:<6} {c2:<6} {idiff:<12} {odiff}")
    output_diffs[odiff] = output_diffs.get(odiff, 0) + 1

print()
print("=== Output Difference Distribution ===")
for diff, count in sorted(output_diffs.items()):
    print(f"  Output diff {diff}: occurred {count} times")

most_common = max(output_diffs, key=output_diffs.get)
print()
print(f"Most common output difference: {most_common}")
print("Attacker uses this pattern to guess the key!")