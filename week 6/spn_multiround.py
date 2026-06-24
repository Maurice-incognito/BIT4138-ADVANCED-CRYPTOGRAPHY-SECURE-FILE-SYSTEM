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

def int_to_nibbles(v):
    return [(v >> (4*(3-i))) & 0xF for i in range(4)]

def nibbles_to_bits(nibbles):
    bits = []
    for n in nibbles:
        bits += [(n >> (3-i)) & 1 for i in range(4)]
    return bits

def bits_to_int(bits):
    val = 0
    for b in bits:
        val = (val << 1) | b
    return val

def spn_encrypt(plaintext, keys, rounds=2):
    state = plaintext
    print(f"Starting value: {hex(state)}")
    print()
    for r in range(rounds):
        print(f"--- Round {r+1} ---")
        # Key mixing
        state ^= keys[r]
        print(f"  After key XOR  : {hex(state)}")
        # Substitution
        nibbles = int_to_nibbles(state)
        subst   = substitute(nibbles)
        print(f"  After sub      : {[hex(n) for n in subst]}")
        # Permutation
        bits    = nibbles_to_bits(subst)
        perm    = permute(bits, P_TABLE)
        state   = bits_to_int(perm)
        print(f"  After permute  : {hex(state)}")
        print()
    # Final key mixing
    state ^= keys[rounds]
    print(f"Final key XOR  : {hex(state)}")
    return state

plaintext = 0x1234
keys      = [0xABCD, 0x5678, 0x9EF0]  # one key per round + final

print("=== Multi-Round SPN Encryption ===")
print()
ciphertext = spn_encrypt(plaintext, keys, rounds=2)
print()
print(f"Plaintext  : {hex(plaintext)}")
print(f"Ciphertext : {hex(ciphertext)}")
print("Multi-round SPN encryption complete!")