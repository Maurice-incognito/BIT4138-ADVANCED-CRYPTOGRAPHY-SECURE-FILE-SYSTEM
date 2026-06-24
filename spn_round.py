# Student: [Your Name] - BIT4138

sbox = {
    0:14, 1:4,  2:13, 3:1,
    4:2,  5:15, 6:11, 7:8,
    8:3,  9:10, 10:6, 11:12,
    12:5, 13:9, 14:0, 15:7
}

P_TABLE = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]

def substitute(nibbles):
    return [sbox[n] for n in nibbles]

def permute(bits, table):
    return [bits[table[i]] for i in range(len(table))]

def int_to_nibbles(value, count=4):
    bits = [(value >> (4 * (count - 1 - i))) & 0xF for i in range(count)]
    return bits

def nibbles_to_bits(nibbles):
    bits = []
    for n in nibbles:
        bits += [(n >> (3 - i)) & 1 for i in range(4)]
    return bits

def bits_to_nibbles(bits):
    nibbles = []
    for i in range(0, len(bits), 4):
        val = 0
        for b in bits[i:i+4]:
            val = (val << 1) | b
        nibbles.append(val)
    return nibbles

# Input
plaintext = 0xABCD
key       = 0x1234

print("=== Single SPN Round ===")
print()
print(f"Plaintext (hex)  : {hex(plaintext)}")
print(f"Round Key (hex)  : {hex(key)}")

# Step 1: Key mixing (XOR)
mixed = plaintext ^ key
print()
print(f"After Key XOR    : {hex(mixed)}")

# Step 2: Substitution
nibbles    = int_to_nibbles(mixed)
subst      = substitute(nibbles)
print(f"After Substitution (nibbles): {subst}")

# Step 3: Permutation
bits       = nibbles_to_bits(subst)
permuted   = permute(bits, P_TABLE)
out_nibbles = bits_to_nibbles(permuted)
result     = sum(n << (4 * (3 - i)) for i, n in enumerate(out_nibbles))

print(f"After Permutation: {hex(result)}")
print()
print("=== Round Summary ===")
print(f"Input    : {hex(plaintext)}")
print(f"Output   : {hex(result)}")
print("One SPN round completed successfully!")